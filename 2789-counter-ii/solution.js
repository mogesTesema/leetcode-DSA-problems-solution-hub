/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    let d=init
    return {
        increment: ()=>{
            return ++d;

        },
        decrement:()=>{
            return --d;
        },
        reset:()=>{
            d=init
            return d;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
