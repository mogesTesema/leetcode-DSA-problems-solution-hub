/**
 * @param {number} n
 * @return {Function} counter
 */

var createCounter = function(n) {
     let p=-1
    return function() {
        p+=1
        return n+p
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
