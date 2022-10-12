setImmediate(demoFunction);

function demoFunction(){
	console.log('At what time the training get over for the day ?');
}

setTimeout(function(){
console.log('Learning Node JS from TT');
},1000);
console.log(' After setTimeout() ');