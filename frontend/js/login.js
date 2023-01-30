function login() {
    let server = sessionStorage.getItem("server")
    let email = $("#emailField").val()
    let password = $("#passwordField").val()

    let data = JSON.stringify({
        email: email,
        password: password
    })

    ajaxFunction("login", "POST", data, function(returnContent) {
        if (returnContent.result === "success") {
            sessionStorage.setItem("login", returnContent.user.email)
            sessionStorage.setItem("jwt", returnContent.token)
            sessionStorage.setItem("user_permission", returnContent.user.permission.name)
            alert(`Successfully logged in! Welcome ${returnContent.user.name}!`)
            return displayInitialMenu(returnContent.user.permission.name.toLowerCase())
        }
    })
}

function logOut() {
    sessionStorage.removeItem("login")
    sessionStorage.removeItem("jwt")
    sessionStorage.removeItem("user_permission")
    $(".content-head").empty()
    $(".content-body").empty()
    $(".products").empty()
    $(".content-body").append(`
    <form onsubmit="return false">
        <label for="emailField">Write your email</label><br>
        <input id="emailField" type="text" placeholder="Email"><br><br>
        <label for="passwordField">Write your password</label><br>
        <input id="passwordField" type="password" placeholder="Password"><br><br>
        <button onclick="login()">Login</button>
    </form>
    `)
}