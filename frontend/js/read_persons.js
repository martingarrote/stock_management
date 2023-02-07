function displayButtons() {
    $(".manage-body").empty()
    $(".manage-body").append(`
    <p>Search by:</p>
    <select id="search-persons" value="Search by">
        <option value="all-persons">All persons</option>
        <option value="admin">Admin permission</option>
        <option value="worker">Worker permission</option>
        <option value="default">Default permission</option>
    </select>
    <button onclick="readPersons()">GO</button>
    `)
}

function readPersons() {
    $(".persons").empty()
    let value = $("#search-persons").find(":selected").val()
    let route
    if (value === "all-persons") {
        route = `persons`
    }
    else if (value === "admin") {
        route = `persons/search/permission/3`
    }
    else if (value === "worker") {
        route = `persons/search/permission/2`
    }
    else if (value === "default") {
        route = `persons/search/permission/1`
    }
    ajaxFunction(route, "GET", null, function (returnContent) {
        if (returnContent.result === "success") {
            $(".persons").append(`
            <table class="persons-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Permission</th>
                    </tr>
                </thead>
                <tbody id="persons-table-body">

                </tbody>
            </table>
            `)
            for (p of returnContent.details) {
                $("#persons-table-body").append(
                    displayPerson(p.id, p.name, p.email, p.permission.name, p.permission.id)
                )
            }
        }
        else {
            alert(`${returnContent.result}: ${returnContent.details}`)
        }
    })
}