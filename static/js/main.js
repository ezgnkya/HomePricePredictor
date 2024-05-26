(function ($) {
    "use strict";

    // Form validation
    var contactForm = function () {
        if ($('#contactForm').length > 0) {
            $("#contactForm").validate({
                rules: {
                    room: "required",
                    age: "required",
                    neighborhood: "required",
                    gross_square: {
                        required: true,
                        number: true,
                        min: 40,
                        max: 220
                    }
                },
                messages: {
                    room: "Oda sayısı seçiniz",
                    age: "Bina yaşı seçiniz",
                    neighborhood: "Mahalle seçiniz",
                    gross_square: {
                        required: "Brüt metre kare bilgisi zorunludur",
                        number: "Lütfen geçerli bir sayı giriniz",
                        min: jQuery.validator.format("En az {0} olmalıdır"),
                        max: jQuery.validator.format("En fazla {0} olabilir")
                    }
                },
                submitHandler: function (form) {
                    var room = $("select[name='room']").val();
                    var age = $("select[name='age']").val();
                    var neighborhood = $("select[name='neighborhood']").val();
                    var gross_square = $("input[name='gross_square']").val();

                    var data = {
                        "room": room,
                        "age": age,
                        "neighborhood": neighborhood,
                        "gross_square": gross_square
                    };

                    $(".submitting").css('display', 'block').text('Tahmin Ediliyor...');

                    // Send AJAX request
                    $.ajax({
                        type: "POST",
                        url: "/predict",
                        contentType: "application/json",
                        data: JSON.stringify(data),
                        success: function (response) {
                            $("#tahmin-sonuc").html("<p>Tahmini Fiyat: " + response.predicted_price + " TL</p>");
                        },

                        complete: function () {
                            $(".submitting").css('display', 'none');
                        }
                    });
                }
            });
        }
    };
    contactForm();

    $("#predictButton").click(function () {
        $("#contactForm").submit();
    });
})(jQuery);
