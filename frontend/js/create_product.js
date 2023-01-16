$(document).on("click", "#createProduct", function() {
    let name = $("#nameField").val()
    let description = $("#descriptionField").val()
    let perishable = booleanFixer($("#perishableField").val())
    let freezable = booleanFixer($("#freezableField").val())
    let price = parseFloat($("#priceField").val())
    let expired = booleanFixer($("#expiredField").val())
    let validity = $("#validityField").val()

    if (validity != "") {
        data = JSON.stringify({name: name, description: description,
        is_perishable: perishable, freezable: freezable, price: price, 
        expired: expired, validity: validity})
    }
    else {
        data = JSON.stringify({name: name, description: description,
        is_perishable: perishable, freezable: freezable, price: price,
        expired: expired, validity: null})
    }
    
    ajaxFunction("new_product", "POST", data, function() {
        alert("The product has been created!")
    })
})