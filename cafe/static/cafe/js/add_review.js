function validate_form() {
    var form = document.forms["new_cafe"];

    if (form["plug"].value === "") {
        alert("Select plug status!");
        return false;
    }

    if (form["wifi"].value === "") {
        alert("Select plug status!");
        return false;
    }

	return true;
}
