//const { Connection, Request } = require("tedious");

// Create connection to database
const config = {
    authentication: {
      options: {
        userName: "db", // update me
        password: "welcome@123" // update me
      },
      type: "default"
    },
    server: "mis-db.database.windows.net", // update me
    options: {
      database: 'MIS_DB', //update me
      encrypt: true
    }
  };

/*   const connection = new Connection(config);
  
  // Attempt to connect and execute queries if connection goes through
  connection.on("connect", err => {
    if (err) {
      console.error(err.message);
    } else {
        console.log('Connected to MIS_DB...');
    }
    //connection.close();
  });
  
  connection.connect(); */

  module.exports = config
