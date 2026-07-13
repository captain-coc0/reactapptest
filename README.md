# Notes
to build a react app in your project, run this in root:
npm create vite@latest frontend -- --template react

then go to /frontend, install npm:
npm install

run npm:
npm run dev

POST: used when something in the backend needs to be changed
GET: used to inconsequently pull data
PUT: upload data that will change a specific pre existing piece of data.

callbacks:
javascript functions will execute with little regard to order of call. if a function called first may complete later than the second called function and produce output last. with callbacks, we can pass a function into a function as an argument, and the main function will execute and then call the passed in function to ensure order of execution is correct. we use arrow functions because we often only need these callback functions once.

useState: 
persistent state across multiple renders. when a state value changes through ui interaction a rerender is triggered and useeffect will be ran again, which can be used for any background processing needed


useEffect:
a react functionality. useEffect is a function call which takes a callback function as an input and runs code on every rerender

selector elements:
selector elements which prompt a dropdown list, color selector, etc., have an attribute called "onChange". the callback function can take an argument called "event" and the setter function can take a parameter which is "event.target.value"

