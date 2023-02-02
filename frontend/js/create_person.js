function newAccountMenu() {
    $(".content-body").empty()
    $(".content-body").append(`
    <form onsubmit="return false">
        <label for="personNameField">Write your name</label><br>
        <input id="personNameField" type="text" placeholder="Name"><br><br>
        <label for="personEmailField">Write your email</label><br>
        <input id="personEmailField" type="text" placeholder="Email"><br><br>
        <label for="personPasswordField">Write your password</label><br>
        <input id="personPasswordField" type="password" placeholder="Password"><br><br>
        <label for="personPasswordField2">Repeat your password</label><br>
        <input id="personPasswordField2" type="password" placeholder="Password second time"><br><br>
        <button id="createAccount">Create Account</button>
    </form>
    `)
}

$(document).on("click", "#createAccount", function() {

    let name = $("#personNameField").val()
    let email = $("#personEmailField").val()
    let password = $("#personPasswordField").val()
    let password2 = $("#personPasswordField2").val()

    if (password === password2) {
        data = JSON.stringify({
            name: name,
            email: email,
            password: password
        })

        ajaxFunction("create_person", "POST", data, function (returnContent) {
            if (returnContent.result === "success") {
                alert("Your account has been successfully created")
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
        })
    }
    else {
        $("#personPasswordField").val("")
        $("#personPasswordField2").val("")
        alert("Passwords are not the same")
    }
})