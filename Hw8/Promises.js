var promise = new Promise(function(resolve, reject) {
    setTimeout(function() {
        resolve('hello world');
    }, 5000);
});

promise.then(function success(data) {
    console.log(data);
}, function error(data) {
    console.error(data);
});
