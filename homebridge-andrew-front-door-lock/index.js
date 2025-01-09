const axios = require('axios');
const { AccessoryPlugin, Service, Characteristic } = require('hap-nodejs');

class AndrewFrontDoorLockAccessory {
    constructor(log, config) {
        this.log = log;
        this.config = config;

        // Server endpoints
        this.serverUrl = config.serverUrl;
        this.unlockEndpoint = `${this.serverUrl}/unlock`;
        this.statusEndpoint = `${this.serverUrl}/get_status`;

        // Initial state
        this.locked = true;

        // HomeKit service and characteristic
        this.service = new Service.LockMechanism(config.name);

        // Current Lock State
        this.service
            .getCharacteristic(Characteristic.LockCurrentState)
            .on('get', this.handleGetCurrentLockState.bind(this));

        // Target Lock State
        this.service
            .getCharacteristic(Characteristic.LockTargetState)
            .on('get', this.handleGetTargetLockState.bind(this))
            .on('set', this.handleSetTargetLockState.bind(this));
    }

    // Get the current lock state
    async handleGetCurrentLockState(callback) {
        try {
            const response = await axios.get(this.statusEndpoint);
            this.locked = !response.data.unlocked; // Assume unlocked=true means unlocked
            this.log(`Current lock state: ${this.locked ? 'LOCKED' : 'UNLOCKED'}`);
            callback(null, this.locked ? Characteristic.LockCurrentState.SECURED : Characteristic.LockCurrentState.UNSECURED);
        } catch (error) {
            this.log('Error getting current lock state:', error.message);
            callback(error);
        }
    }

    // Get the target lock state
    handleGetTargetLockState(callback) {
        this.log(`Target lock state: ${this.locked ? 'LOCKED' : 'UNLOCKED'}`);
        callback(null, this.locked ? Characteristic.LockTargetState.SECURED : Characteristic.LockTargetState.UNSECURED);
    }

    // Set the target lock state
    async handleSetTargetLockState(state, callback) {
        try {
            if (state === Characteristic.LockTargetState.UNSECURED) {
                this.log('Unlocking the door...');
                await axios.get(this.unlockEndpoint);
                this.locked = false;
            } else {
                this.log('Locking the door...');
                // Assuming locking happens automatically after the unlock timeout
                this.locked = true;
            }
            callback(null);
        } catch (error) {
            this.log('Error setting lock state:', error.message);
            callback(error);
        }
    }

    // Identify the accessory
    identify(callback) {
        this.log('Identify called for AndrewFrontDoorLockAccessory');
        callback();
    }

    // Return the service
    getServices() {
        return [this.service];
    }
}

module.exports = (api) => {
    api.registerAccessory('homebridge-andrew-front-door-lock', 'AndrewFrontDoorLockAccessory', AndrewFrontDoorLockAccessory);
};
