function deletePerson(id) {
    ajaxFunction(`delete_person/${id}`, "DELETE", null, function(returnContent) {
        if (returnContent.result === "success") {
            $(`#pline-${id}`).remove()
            alert(`The person with ID ${id} has been deleted.`)
        }
        else {
            alert(`${returnContent.result}: ${returnContent.details}`)
        }
    })
}