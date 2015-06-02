# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tests import common


class TestMgmtsystemHazardRisk(common.TransactionCase):

    def setUp(self):
        super(TestMgmtsystemHazardRisk, self).setUp()

        self.computation_model = self.env['mgmtsystem.hazard.risk.computation']
        self.company_model = self.env['res.company']

        self.company = self.company_model.create({
            'name': 'Test Company',
        })

    def test_company_default_risk_computation_id(self):
        default_risk_computation = self.env().ref(
            'mgmtsystem_hazard_risk.risk_computation_a_times_b_times_c')

        self.assertEqual(
            self.company.risk_computation_id,
            default_risk_computation)
