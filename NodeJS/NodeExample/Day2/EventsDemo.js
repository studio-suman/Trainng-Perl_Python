var refEvents = require('events');

var objEventEmitter = new refEvents.EventEmitter();

var feelingSleepy = function(){
	console.log('Boring Training');
	objEventEmitter.emit('webExtrng');
}
objEventEmitter.on('webExtrng',function(){
	console.log(' Node JS Training ');
});
objEventEmitter.on('partResp',feelingSleepy);
objEventEmitter.addListener('partResp',function(){
	console.log('People are feeling comfortable with Node JS');
});
objEventEmitter.emit('partResp');

objEventEmitter.removeListener('partResp',feelingSleepy);
console.log('Initiating for the Second time ');
objEventEmitter.emit('partResp');

