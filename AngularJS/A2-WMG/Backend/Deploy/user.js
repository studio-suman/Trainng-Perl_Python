class userDb {
    constructor(id,cName,cContactNumber,cEmail,cPassword,cStatus,cRole) {
        this.id = id;
        this.name = cName;
        this.contactNumber = cContactNumber;
        this.email = cEmail;
        this.password = cPassword;
        this.status = cStatus;
        this.status = cRole;    
    }
}

module.exports = userDb