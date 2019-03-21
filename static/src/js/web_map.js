odoo.define('location.web_map', function (require) {
    "use strict";
var my_attendances = require('hr_attendance.my_attendances');

my_attendances.include({
        update_attendance: function () {
                var self = this;
                        this._rpc({
                model: 'hr.employee',
                method: 'attendance_manual',
                args: [[self.employee.id], 'hr_attendance.hr_attendance_action_my_attendances'],
            })
            .then(function() {
                if(navigator.geolocation){
                    navigator.geolocation.getCurrentPosition(function(position) {
                        var pos = {
                            lat: position.coords.latitude,
                            lng: position.coords.longitude,

                        };

                        var action = {
                            type: 'ir.actions.act_window',
                            res_model: 'meeting.location',

                            views: [[false, 'form']],
                            context: {
                                'default_lat_ip': pos.lat,
                                'default_lon_ip': pos.lng,
                            },
                        };
                        self.do_action(action);
                     })
        }
});
            },
    });


});
