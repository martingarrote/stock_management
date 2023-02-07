let editing = false

let startName
let startEmail
let startPermission
let startPermissionId

let newName
let newEmail
let newPermission
let newPermissionId

function getPermissionName(permissionId) {
    if (permissionId === "3") {
        return "admin"
    }
    else if (permissionId === "2") {
        return "worker"
    }
    else if (permissionId === "1") {
        return "default"
    }
}

function cancelModification(id) {   
    editing = false
    $(`#pName-${id}`).html(startName)
    $(`#pEmail-${id}`).html(startEmail)
    $(`#pPermission-${id}`).html(startPermission)

    $(`#operations-${id}`).empty()
    $(`#operations-${id}`).append(`
        <i id="updatePersonIcon-${id}" class="fa-solid fa-pen-to-square" title="Update person" onclick="startPersonUpdate(${id})"></i>
    `)
    if (startPermissionId != 3) {
        $(`#operations-${id}`).append(`
            <i id="deletePersonIcon-${id}" class="fa-solid fa-trash" title="Delete person" onclick="deletePerson(${id})"></i>
        `)
    }
}

function saveModification(id) {
    editing = false
    $(`#pName-${id}`).html(newName)
    $(`#pEmail-${id}`).html(newEmail)
    $(`#pPermission-${id}`).html(newPermission)

    $(`#operations-${id}`).empty()
    $(`#operations-${id}`).append(`
        <i id="updatePersonIcon-${id}" class="fa-solid fa-pen-to-square" title="Update person" onclick="startPersonUpdate(${id})"></i>
    `)
    if (startPermissionId != 3) {
        $(`#operations-${id}`).append(`
            <i id="deletePersonIcon-${id}" class="fa-solid fa-trash" title="Delete person" onclick="deletePerson(${id})"></i>
        `)
    }
}

function startPersonUpdate(id) {
    if (!editing) {

        editing = true

        startName = $(`#pName-${id}`).text()
        startEmail = $(`#pEmail-${id}`).text()
        startPermissionId = $(`#pPermission-${id}`).attr("class").slice(11)
        startPermission = getPermissionName(startPermissionId)

        $(`#pName-${id}`).html(`<input type="text" id="upNameField" value="${startName}">`)
        $(`#pEmail-${id}`).html(`<input type="text" id="upEmailField" value="${startEmail}">`)
        $(`#pPermission-${id}`).html(`
        <select id="new-permission-select">
            <option value="3">Admin permission</option>
            <option value="2">Worker permission</option>
            <option value="1">Default permission</option>
        </select>
        `)
        $("#new-permission-select").val(startPermissionId)

        $(`#updatePersonIcon-${id}`).attr("class", "fa-solid fa-check")
        $(`#updatePersonIcon-${id}`).attr("onclick", `processUpdatedData(${id})`)
        $(`#updatePersonIcon-${id}`).attr("title", "Save changes")
        $(`#operations-${id}`).append(`
            <i id="resetChanges-${id}" class="fa-solid fa-x" title="Reset changes", onclick="cancelModification(${id})"></i>
        `)
        if (startPermissionId != 3) {$(`#deletePersonIcon-${id}`).hide()}
    }

    else {
        alert("You cannot edit two user at the same time")
    }
}



function processUpdatedData(personId) {
    newName = $("#upNameField").val()
    newEmail = $("#upEmailField").val()
    newPermissionId = $("#new-permission-select").find("option:selected").val()
    newPermission = getPermissionName(newPermissionId)

    const data = {}

    if (startName != newName) {
        data.name = newName
    }
    if (startEmail != newEmail) {
        data.email = newEmail
    }
    if (startPermissionId != newPermissionId) {
        data.permission_id = newPermissionId
    }

    if (Object.keys(data).length === 0) {
        alert("Don't have changes.")
        cancelModification(personId)
    }

    else if (Object.keys(data).length > 0) {
        saveModification(personId)
        ajaxFunction(`update_person/${personId}`, "PUT", JSON.stringify(data), function (returnContent) {
            if (returnContent.result === "success") {
                alert("The person has been updated.")
            }
            else {
                alert(`${returnContent.result}: ${returnContent.details}`)
            }
        })
    }
    
}