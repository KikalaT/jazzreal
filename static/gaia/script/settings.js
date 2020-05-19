// Helper functions for saving and loading user settings with localstorage.
settings = (function() {
	// Used for seperating settings on the same domain
	const prefix = "Gaia_v1.0";
	
	// Default values for various user settings.
	const defaultValues = {
		"documentContent": "JAZZ\n\t1 Caractéristiques\n\t\t1.1 Caractéristiques générales\n\t\t1.2 Importance de l'improvisation\n\t\t1.3\ Débats\n\t2 Étymologie\n\t3 Histoire\n\t\t3.1 Origines\n\t\t\t3.1.1 Musique et danses des esclaves\n\t\t\t3.1.2 Influences afro-caribéennes\n\t\t3.2 Ragtime et blues (1890-1910)\n\t\t3.3 Jazz Nouvelle-Orléans et Dixieland (1910-1930)\n\t\t3.4 Du swing au bebop\n\t\t3.5 Cool jazz, hard bop, jazz modal, free jazz (années 1950)\n\t\t3.6 Third Stream\n\t\t3.7 Jazz fusion et sous-genres\n\t\t3.8 Smooth jazz, nu jazz et jazz rap\n\t\t3.9 Jazz contemporain\n\t4 Caractères clés\n\t5 Principaux artistes\n\t\t5.1 Compositeurs\n\t\t5.2 Musiciens\n\t\t5.3 Chanteuses\n\t\t5.4 Chanteurs\n\t\t5.5 Formations\n\t6 Diffusion\n\t\t6.1 Clubs de jazz\n\t\t\t6.1.1 New York\n\t\t\t6.1.2 Paris\n\t\t\t6.1.3 Autres villes\n\t\t6.2 Festivals\n\t\t6.3 Enregistrements et labels\n\t\t6.4 Dans les médias\n\t\t6.5 Presse spécialisée\n\t\t6.6 L'enseignement du jazz dans un cadre formel\n\t7 Influence\n\t\t7.1 Musique\n\t\t7.2 Littérature\n\t\t7.3 Arts picturaux\n\t\t7.4 Cinéma\n\t8 Bibliographie\n\t\t8.1 En français\n\t\t8.2 En anglais\n\t9 Notes et références\n\t10 Articles connexes\n\t11 Liens externes", 
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
