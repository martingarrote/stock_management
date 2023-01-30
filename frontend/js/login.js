function sucessfullyLoggedIn() {
    console.log("oii")
    $(".content-body").empty()
    $(".content-head").append(`
        <button onclick="returnToDefault()">HOME</button>
        <button onclick="displayContent('create')">CREATE</button>
        <button onclick="displayContent('read')">READ</button>
        <button onclick="displayContent('update')">UPDATE</button>
        <button onclick="displayContent('delete')">DELETE</button>
    `)
    $(".content-body").append(`
        <p>Press an button to start to testing the program</p>
    `)
    return alert("successfully logged in")
}

function login() {
    let server = sessionStorage.getItem("server")
    let email = $("#emailField").val()
    let password = $("#passwordField").val()

    let data = JSON.stringify({
        email: email,
        password: password
    })

    ajaxFunction("login", "POST", data, function() {sucessfullyLoggedIn()})

}