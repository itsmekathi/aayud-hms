(function () {
    'use strict';
    angular.module('app')
        .directive('customModal', ['ModalService', function (ModalService) {
            function link(scope, element, attrs) {
                // ensure id attribute exists
                if (!attrs.id) {
                    console.error('modal must have an id');
                    return;
                }
                // move element to bottom of page (just before </body>) so 
                // it can be displayed above everything else
                element.appendTo('body');

                // close modal on background click
                element.on('click', function (e) {
                    var target = $(e.target);
                    if (!target.closest('.custom-modal-body').length) {
                        scope.$evalAsync(Close);
                    }
                    if (target.hasClass('custom-modal-close-button')) {
                        scope.$evalAsync(Close);
                    }
                });

                // add self (this modal instance ) to the modal service so 
                // it's accessible from controller
                var modal = {
                    id: attrs.id,
                    open: Open,
                    close: Close
                };
                ModalService.Add(modal);

                // remove self from modal service when directive is destroyed
                scope.$on('$destory', function () {
                    ModalService.Remove(attrs.id);
                    element.remove();
                });

                // open modal
                function Open() {
                    element.show();
                    $('body').addClass('custom-modal-open');
                }

                // close modal
                function Close() {
                    element.hide();
                    $('body').removeClass('custom-modal-open');
                }
            }
            return {
                link: link
            }
        }]);
})();