function updateProduct(selected) {
    if (selected === "expired_products") {
        ajaxFunction("update_expired_products", "PUT", null, function() {alert("Expired products has been update")})
    }
    else if (selected === "specific_product") {
        $(".content-body").empty()
        displayContent("update")
        $(".content-body").append(`
        <form onsubmit="return false">
        <p>Give the informations:</p>
        <input id="productId" type="number" min="1" placeholder="Product ID"><br><br>
        <input id="nameField" type="text" placeholder="Name"><br>
        <input id="descriptionField" type="text" placeholder="Description"><br>
        <input id="perishableField" type="text" placeholder="Perishable"><br>
        <input id="freezableField" type="text" placeholder="Freezable"><br>
        <input id="priceField" type="text" placeholder="Price"><br>
        <input id="expiredField" type="text" placeholder="Expired"><br>
        <input id="validityField" type="date" placeholder="Validity"> <button id="noValidity">Remove validity</button><br>
        <button id="updateProduct" type="submit">Update Product</button>
        </form>
        `)
        
        let productToUpdate
        let name
        let description
        let perishable
        let freezable
        let price
        let expired
        let validity
    
        $(document).on("click", "#noValidity", function() {
            validity = "noValidity"
        })
    
        $(document).on("click", "#updateProduct", function() {
            
            productToUpdate = $("#productId").val()
            name = $("#nameField").val()
            description = $("#descriptionField").val()
            perishable = booleanFixer($("#perishableField").val())
            freezable = booleanFixer($("#freezableField").val())
            expired = booleanFixer($("#expiredField").val())
        
            if ($("#priceField").val() != "") {
                parseFloat($("#priceField").val())
            }
    
            if (validity != "noValidity") {
                validity = $("#validityField").val()
            }
        
            let values = {
                name: name,
                description: description,
                is_perishable: perishable,
                freezable: freezable,
                price: price,
                expired: expired,
                validity: validity
            }
        
            for (key in values) {
                if (values[key] === null || values[key] === undefined || values[key].length < 1 || values[key] < 0) {
                    delete values[key]
                }
            }
            ajaxFunction(`update_product/${productToUpdate}`, "PUT", JSON.stringify(values), function() {
                alert(`The product with ID ${productToUpdate} has been updated.`)
            })
        })
    }
}