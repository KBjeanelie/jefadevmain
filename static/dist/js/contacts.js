$('#form_contact #submit_contact').click(function(e) {
    e.preventDefault();

    var cheminAjax = document.getElementById('soumission_form').innerHTML;
    var formData = new FormData($('#form_contact')[0]);
    formData.append('op', 'save_contact');

    $.ajax({
        type: 'POST',
        url: cheminAjax,
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            if (data["resultat"] === "SUCCES") {
                $('#form_contact #message').html(
                    '<div class="alert alert-success">' + data["message"] + '</div>'
                );
                $('#form_contact')[0].reset();
            } else if (data["resultat"] === "WARNING") {
                $('#form_contact #message').html(
                    '<div class="alert alert-warning">' + data["message"] + '</div>'
                );
            } else if (data["resultat"] === "FATAL") {
                $('#form_contact #message').html(
                    '<div class="alert alert-danger">' + data["message"] + '</div>'
                );
            }
        },
        error: function(xhr, status, error) {
            $('#form_contact #message').html(
                '<div class="alert alert-danger">Erreur lors de l\'envoi. Veuillez réessayer.</div>'
            );
            console.log(xhr.responseText, status, error);
        }
    });
});