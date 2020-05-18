// Helper functions for saving and loading user settings with localstorage.
settings = (function() {
	// Used for seperating settings on the same domain
	const prefix = "ROSO-MIND_v1.0";
	
	// Default values for various user settings.
	const defaultValues = {
		"documentContent": "On Green Dolphin St.\n\t(A)\n\t\tEbmaj7(1) | Ebmaj7(1) | Ebm7(1) | Ebm7(1)\n\t\tF7/Eb(1) | Emaj7/Eb(1) | Ebmaj7(1) | C7(1)|\n\t(B)\n\t\tFm7(1) | Bb7alt(1) | Ebmaj7(1) | Ebmaj7(1)\n\t\tAbm7(1) | Db7alt(1) | Gbmaj7(1) | Fm7(2) Bb7(2)|\n\t(C)\n\t\tFm7(2) Fm7/Eb(2) | Dm7b5(2) G7b9(2) | Cm7(2) Cm7/Bb(2) | Am7b5(2) D7b9(2)\n\t\tGm7(2) C7(2) | Fm7(2) Bb7(2) | Eb6(1) | Fm7(2) Bb7(2)|",
		"documentTitle": "document sans nom"
	};

	// Used for converting settings values to actual font-familys.
	const fontFamilyMap = {
		"monospace": "monospace",
		"sans-serif": "sans-serif",
		"serif": "serif",
	};

	// Get the setting with the specified key. If the setting is null, use the default value.
	function getSetting(key) {
		let setting;
		try {
			setting = JSON.parse(localStorage.getItem(prefix+key));
		} catch (exception) {
			// Ignored
		}
		if (!setting || setting == "") {
			setting = getDefaultValue(key);
			setSetting(key, setting);
		}
		return setting;
	}

	// Set the setting with the specified key to the specified value.
	function setSetting(key, value) {
		if (!value) {
			value = getDefaultValue(key);
		}
		try {
			localStorage.setItem(prefix+key, JSON.stringify(value));
		} catch (exception) {
			console.error(`Erreur d'enregistrement.\nKey: ${key}\nValue: ${value}\n`);
		}
	}

	// Get the default value of the setting with the specified key.
	function getDefaultValue(key) {
		if (key in defaultValues) {
			return defaultValues[key];
		}
	}

	// Reset all the settings to their default values.
	function reset() {
		for (let key in defaultValues) {
			setSetting(key, getDefaultValue(key));
		}
	}

	return {
		getSetting,
		setSetting,
		fontFamilyMap,
		getDefaultValue,
		reset
	};
}());
