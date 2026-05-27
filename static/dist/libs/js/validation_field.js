// document.addEventListener("DOMContentLoaded", function () {
//        var regExpMask = IMask(document.getElementById('id_tel2'),
//            {
//               // mask: /^[465]\d{0,9}$/
//               mask: function (value) {
//                   var reg = new RegExp("^0$|^0[645]$|^0[645][0-9]{1,7}$|^2420$|^2420[645]$|^2420[645][0-9]{1,7}$|^2$|^24$|^242$|^2420$");
//                   var test = reg.test(value);
//                   return test
//               }
//            });
//        var regExpMask = IMask(document.getElementById('id_tel2_ent'),
//            {
//               // mask: /^[465]\d{0,9}$/
//               mask: function (value) {
//                   var reg = new RegExp("^0$|^0[645]$|^0[645][0-9]{1,7}$|^2420$|^2420[645]$|^2420[645][0-9]{1,7}$|^2$|^24$|^242$|^2420$");
//                   var test = reg.test(value);
//                   return test
//               }
//            });
//
// });

(function(window, document, $) {
	'use strict';

	// Date dd/mm/yyyy
	$('.date-inputmask').inputmask("dd/mm/yyyy");

	//Phone mask
	$('.phone-inputmask').inputmask("(242) 0(4)|(5)|(6) 999 9999");

	$('.phone-inputmask-mtn').inputmask("(242) 06 999 9999");

	//NIU 16
	$('.niu-inputmask').inputmask("P9999999999999999");

	//CNI
	$('.cni-inputmask').inputmask("(AA9999XXXXXXX)|(AA9999XXXXXXX-99)",{
		definitions: {
			"X": {
				validator: "[0-9A-Za-z]",
				casing: "upper"
			}
		}
	});

	//RCCM
	$('.rccm-inputmask').inputmask("RCCM CG XXX 99 X 999",{
		definitions: {
			"X": {
				validator: "[A-Za-z]",
				casing: "upper"
			}
		}
	});

	//Carte de résident
	$('.cr-inputmask').inputmask("999999999");

	//Passeport
	$('.passeport-inputmask').inputmask("XXXXXXXXX",{
		definitions: {
			"X": {
				validator: "[0-9A-Za-z]",
				casing: "upper"
			}
		}
	});





	// Another Date mm-dd-yyyy
	$('.international-inputmask').inputmask("+9(999)999-9999");

	//Phone with extra
	$('.xphone-inputmask').inputmask("(999) 999-9999 / x999999");

	// Purchase Order
	$('.purchase-inputmask').inputmask("aaaa 9999-****");

	// Credit Card Number
	$('.cc-inputmask').inputmask("9999 9999 9999 9999");

	// SSN
	$('.ssn-inputmask').inputmask("999-99-9999");

	// ISBN
	$('.isbn-inputmask').inputmask("999-99-999-9999-9");

	// Currency in USD
	$('.currency-inputmask').inputmask("$9999");

	// Percentage
	$('.percentage-inputmask').inputmask("99%");

	// Decimal
	$('.decimal-inputmask').inputmask({ "alias": "decimal" , "radixPoint": "." });
	$('.number-inputmask').inputmask({ "alias": "integer","radixPoint": "" });

	// Email mask
	$('.email-inputmask').inputmask({
		mask: "*{1,20}[.*{1,20}][.*{1,20}][.*{1,20}]@*{1,20}[*{2,6}][*{1,2}].*{1,}[.*{2,6}][.*{1,2}]",
		greedy: false,
		onBeforePaste: function (pastedValue, opts) {
			pastedValue = pastedValue.toLowerCase();
			return pastedValue.replace("mailto:", "");
		},
		definitions: {
			'*': {
				validator: "[0-9A-Za-z!#$%&'*+/=?^_`{|}~/-]",
				cardinality: 1,
				casing: "lower"
			}
		}
	});

	// Optional Mask
	$('.optional-inputmask').inputmask("(99) 9999[9]-9999");

	// JIT Masking
	$('.jit-inputmask').inputmask("mm-dd-yyyy",{ jitMasking: true });

	// Oncomplete
	$('.oncomplete-inputmask').inputmask("d/m/y",{ "oncomplete": function(){ alert('inputmask complete'); } });

	// Onincomplete
	$('.onincomplete-inputmask').inputmask("d/m/y",{ "onincomplete": function(){ alert('inputmask incomplete'); } });

	// Oncleared
	$('.oncleared-inputmask').inputmask("d/m/y",{ "oncleared": function(){ alert('inputmask cleared'); } });

})(window, document, jQuery);


$(".buttons-collection").removeClass()

// =========================================== select
$(document).ready(function () {

// ============================= INPUT MASK
	$("#id_type_piece").change(function (e){
		$('#id_num_piece').val("");


	if($("#id_type_piece").val() == "Passeport"){
		$('#id_num_piece').inputmask("XXXXXXXXX",{definitions: {"X": {validator: "[0-9A-Za-z]", casing: "upper"}}});

	}else if($("#id_type_piece").val() == "Carte Nationale d'identité"){
		$('#id_num_piece').inputmask("(AA9999XXXXXX)|(AA9999XXXXXXX-99)",{definitions: {"X": {validator: "[0-9A-Za-z]", casing: "upper"}}});

	}else if($("#id_type_piece").val() == "Carte de Résident"){
		$('#id_num_piece').inputmask("999999999");

	} else if($("#id_type_piece").val() == "Permis de conduire"){
		$('#id_num_piece').inputmask("XX9999999XX",{definitions:{"X": {validator: "[A-Za-z]", casing: "upper"}}});

	};
});
// ============================= INPUT MASK
	$("#id_type_piece2").change(function (e){
		$('#id_num_piece2').val("");


	if($("#id_type_piece2").val() == "Passeport"){
		$('#id_num_piece2').inputmask("XXXXXXXXX",{definitions: {"X": {validator: "[0-9A-Za-z]", casing: "upper"}}});

	}else if($("#id_type_piece2").val() == "Carte Nationale d'identité"){
		$('#id_num_piece2').inputmask("(AA9999XXXXXX)|(AA9999XXXXXXX-99)",{definitions: {"X": {validator: "[0-9A-Za-z]", casing: "upper"}}});

	}else if($("#id_type_piece2").val() == "Carte de Résident"){
		$('#id_num_piece2').inputmask("999999999");

	} else if($("#id_type_piece2").val() == "Permis de conduire"){
		$('#id_num_piece2').inputmask("XX9999999XX",{definitions:{"X": {validator: "[A-Za-z]", casing: "upper"}}});

	};
});

});









