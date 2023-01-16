$(document).on("click", "#deleteBtn", function() {
    let productToDeleteId = $("#productToDelete").val()
    ajaxFunction(`delete_product/${productToDeleteId}`, "DELETE", null, function() {
        alert(`The product with ID ${productToDeleteId} has been deleted.`)
    })
})