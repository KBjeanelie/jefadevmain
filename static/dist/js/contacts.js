$('#submit').click(function(e) {
    console.log("========== CONTACT FORM ")
        e.preventDefault();

        var cheminAjax = document.getElementById('soumission_form').innerHTML;
        var formData = new FormData($('#form_contact')[0]);
        formData.append('op','save_contact')
    console.log("======= formaData, " , formData)

        $.ajax({
            type: 'POST',
            url: cheminAjax,
            data: formData,
            processData: false, // Ne pas traiter les données
            contentType: false, // Ne pas définir le type de contenu
            success: function(data) {
                if (data["resultat"] == "SUCCES") {
                    // $('#message').html('<div class="alert alert-success">' + response.message + '</div>');
                    success_noti(icontype = "success", position = 'top right', message = data["message"]);

                    // Effacer le formulaire après soumission réussie si nécessaire
                    $('#contact-form')[0].reset();
                } else if (data["resultat"] === "WARNING") {
                    $('#message').html('<div class="alert alert-danger">' + response.message + '</div>');
                }else if (data["resultat"] === "FATAL") {
                success_noti(icontype = "error", position = 'top right', message = data["message"]);
                }
            },
            error: function(xhr, status, error) {
                // $('#message').html('<div class="alert alert-danger">Erreur: ' + error + '</div>');
                 console.log(xhr.responseText, status, e)
            }
        });
    });