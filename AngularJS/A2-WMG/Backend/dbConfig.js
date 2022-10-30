//const { Connection, Request } = require("tedious");

// Create connection to database
  const config = {
        user: "api_user", // update me
        password: "welcome@123", // update me
        server: "mis-db.database.windows.net", // update me
        database: "MIS_DB", //update me
    options: { 
      encrypt: true,
      enableArithAbort: false,
      //type: "default"
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
