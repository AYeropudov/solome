let attributeObject = function () {
    this.dialog = null;
    this.init = function () {
        this.nestListInit();
        let _this = this;
        $(".edit-attr-btn").bind("click", function (e) {
            _this.editItem(e);
        });
        $(".add-attr-btn").bind("click", function (e) {
            _this.addItem(e);
        });
    };

    this.nestListInit = function () {
        jQuery(function ($) {

            $('.dd').nestable();

            $('.dd-handle a').on('mousedown', function (e) {
                e.stopPropagation();
            });

            $('[data-rel="tooltip"]').tooltip();

        });
    };

    this.createModal = function (title, data = false) {
        let _this = this;
        _this.dialog = bootbox.dialog({
            title: title,
            message: '<p><i class="fa fa-spin fa-spinner"></i> Loading...</p>'
        });
        let url = (data)? '/'+data.attr_id: '';
        _this.dialog.init(function () {
            _this.doRequest(
                '/cms/modals/attributes' + url,
                data,
                {method: "GET", dataType: "html"},
                function (result) {
                    _this.dialog.find('.bootbox-body').html(result);
                }
            );
        });
    };

    this.editItem = function (e) {
        let target = $(e.currentTarget);
        this.createModal('Редактировать атрибут', {attr_id: target.data("id")});
    };

    this.addItem = function (e) {
        let target = $(e.currentTarget);
        this.createModal('Добавить атрибут')
    };

    this.doRequest = function (url, data, options, someCall) {
        let result = '';
        let _this = this;
        $.ajax({
            method: options.method,
            dataType: options.dataType,
            data: data,
            url: url
        })
            .done(function (msg) {
                someCall(msg);
            })
            .error(function (msg) {
                someCall(msg);
            });
    }
};

function submitForm(e) {
    let button = $(e);
    let form = $("#"+ button.data("form"));
    let data = new FormData(form[0]);
    $.ajax({
            method: form.data("method"),
            dataType: 'json',
            data: data,
            processData: false,
            contentType: false,
            beforeSend: function(xhr) {xhr.setRequestHeader("X-CSRFToken", $("input[name='csrfmiddlewaretoken']").val());},
            url: form.data("action")
        })
            .done(function (msg) {
               attributesApplication.dialog.modal('hide');
               window.location.reload();
            })
            .error(function (msg) {
                console.log(msg);
            });
}

let attributesApplication = new attributeObject();
attributesApplication.init();






