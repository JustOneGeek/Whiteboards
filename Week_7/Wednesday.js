// I can never remember what my Coding Temple Email address is
// Make a function in JS that will help me test which email address is valid
// Sign up for an account @ https://hunter.io/
// Use their API for verifing emails
// Use AXIOS to access the API
// Write an async function that takes an email address as a string 
// and prints to the console if it is valid or invalid
// Input:
let email1 = "kevinb@codingtemple.com"
// Output
// valid

// Input
let email2 = "kbeier@codingtemple.com"
// Output
// invalid

async function checkEmail(email){
    const axios = require('axios');
    let apiKey="f2e4cb0c969c4531d3540dc27a61575fa76b02e2";
    await axios.get(`https://api.hunter.io/v2/email-verifier?email=${email}&api_key=${apiKey}`)
        .then((response)=>{
            if(response.status==200) console.log(email + ' is ' + response.data.data.status)
            else console.log("Something went wrong!?")})
            .catch((e)=>console.error("We made a Booboo Try Again",e));
}

checkEmail(email1)
checkEmail(email2)

