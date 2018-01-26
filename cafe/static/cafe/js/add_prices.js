function validate_form() {
    var form = document.forms["new_cafe"];
    var americano = parseInt(form["americano"].value);

    if (!(0 < americano && americano < 20000)) {
        alert("Americano price could not be " + americano);
        return false;
    }

	return true;
}

