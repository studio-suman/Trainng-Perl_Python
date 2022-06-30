var refFile = require('fs');

refFile.readdir('C:\\Users\\HSASS\\OneDrive - Wipro\\Desktop\\Trainng-Perl_Python\\NodeJS\\NodeExample',function(refError,objFiles){
   if (refError)
      console.log(' Error in Accessing the directory ' );
   objFiles.forEach(function(refFile){
       console.log(refFile);
   });
});