// LDAP library, documented at http://ldapjs.org/client.html
var ldap = require('ldapjs');
const assert = require('assert').strict;

var client = ldap.createClient({
    url: ["ldap://blr-ec-dc07.wipro.com"]
});

client.bind('hsass@wipro.com', 'ganga@345', function(err) {
  if (err) {
      console.log("Reader bind failed " + err);
      return;
  }
  console.log("Reader bind succeeded(Login Successful)\n");
});

const opts = {
    filter: 'mail=ragupathi.kathiresan@wipro.com',
    scope: 'sub',
    //attributes: ['dn', 'sn', 'cn','samaccountname']
    attributes: ['sn','cn','employeeID']
  };
  
  client.search('dc=wipro,dc=com', opts, (err, res) => {
    assert.ifError(err);
  
    res.on('searchEntry', (entry) => {
      console.log('entry: ' + JSON.stringify(entry.object));
    });
/*    
    res.on('searchReference', (referral) => {
      console.log('referral: ' + referral.uris.join());
    });
    res.on('error', (err) => {
      console.error('error: ' + err.message);
    }); */
    res.on('end', (result) => {
      console.log('status: ' + result.status);
    });
  });
  
  client.unbind((err) => {
    assert.ifError(err);
  });