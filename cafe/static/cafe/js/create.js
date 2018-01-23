function validate_form() {
    console.log("HOHOH")
    var form = document.forms["new_cafe"];
    var americano = parseInt(form["americano"].value);

    if (form["name"].value === "") {
        alert("Name cannot be blank!");
        return false;
    }

	if (form["name"].value.length > 20) {
		alert("잡았다 요놈!");
		return false;
	}

    if (form["address"].value === "") {
        alert("Address cannot be blank!");
        return false;
    }

	if (form["address"].value.length > 20) {
		alert("또 잡았다 요놈!");
		return false;
	}

    if (!(0 < americano && americano < 20000)) {
        alert("Americano price could not be " + americano);
        return false;
    }

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
