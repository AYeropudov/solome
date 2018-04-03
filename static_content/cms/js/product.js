var myDropzone = null;
jQuery(function ($) {
    try {
        Dropzone.autoDiscover = false;

        myDropzone = new Dropzone('div#dropzone', {
            previewTemplate: $('#preview-template').html(),
            url: '/sss/#',
            acceptedFiles: "image/jpg, image/jpeg, image/png, image/gif, image/bmp",
            thumbnailHeight: 220,
            thumbnailWidth: 220,
            maxFilesize: 1.5,

            addRemoveLinks: true,
            dictRemoveFile: 'Удалить',

            dictDefaultMessage:
                '<span class="bigger-150 bolder"><i class="ace-icon fa fa-caret-right red"></i> Drop files</span> to upload \
                <span class="smaller-80 grey">(or click)</span> <br /> \
                <i class="upload-icon ace-icon fa fa-cloud-upload blue fa-3x"></i>'
            ,

            thumbnail: function (file, dataUrl) {
                if (file.previewElement) {
                    $(file.previewElement).removeClass("dz-file-preview");
                    var images = $(file.previewElement).find("[data-dz-thumbnail]").each(function () {
                        var thumbnailElement = this;
                        thumbnailElement.alt = file.name;
                        thumbnailElement.src = dataUrl;
                    });
                    setTimeout(function () {
                        $(file.previewElement).addClass("dz-image-preview");
                    }, 1);
                }
            }

        });


        //simulating upload progress
        var minSteps = 6,
            maxSteps = 60,
            timeBetweenSteps = 100,
            bytesPerStep = 100000;

        myDropzone.uploadFiles = function (files) {
            var self = this;

            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                totalSteps = Math.round(Math.min(maxSteps, Math.max(minSteps, file.size / bytesPerStep)));

                for (var step = 0; step < totalSteps; step++) {
                    var duration = timeBetweenSteps * (step + 1);
                    setTimeout(function (file, totalSteps, step) {
                        return function () {
                            file.upload = {
                                progress: 100 * (step + 1) / totalSteps,
                                total: file.size,
                                bytesSent: (step + 1) * file.size / totalSteps
                            };

                            self.emit('uploadprogress', file, file.upload.progress, file.upload.bytesSent);
                            if (file.upload.progress == 100) {
                                file.status = Dropzone.SUCCESS;
                                self.emit("success", file, 'success', null);
                                self.emit("complete", file);
                                self.processQueue();
                            }
                        };
                    }(file, totalSteps, step), duration);
                }
            }
        }


        //remove dropzone instance when leaving this page in ajax mode
        $(document).one('ajaxloadstart.page', function (e) {
            try {
                myDropzone.destroy();
            } catch (e) {
            }
        });

    } catch (e) {
        alert('Dropzone.js does not support older browsers!');
    }
    ;

    var $overflow = '';
    var colorbox_params = {
        rel: 'colorbox',
        reposition: true,
        scalePhotos: true,
        scrolling: false,
        previous: '<i class="ace-icon fa fa-arrow-left"></i>',
        next: '<i class="ace-icon fa fa-arrow-right"></i>',
        close: '&times;',
        current: '{current} of {total}',
        maxWidth: '100%',
        maxHeight: '100%',
        onOpen: function () {
            $overflow = document.body.style.overflow;
            document.body.style.overflow = 'hidden';
        },
        onClosed: function () {
            document.body.style.overflow = $overflow;
        },
        onComplete: function () {
            $.colorbox.resize();
        }
    };

    $('.ace-thumbnails [data-rel="colorbox"]').colorbox(colorbox_params);
    $("#cboxLoadingGraphic").html("<i class='ace-icon fa fa-spinner orange fa-spin'></i>"); //let's add a custom loading icon


    $(document).one('ajaxloadstart.page', function (e) {
        $('#colorbox, #cboxOverlay').remove();
    });

});