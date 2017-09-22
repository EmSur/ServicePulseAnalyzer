import unittest
import pandas as pd
import os

from SPAn import spanalyzer as spa


class PyServicePulseTests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.csv_sep = "..\\..\\data\\September.xlsx"
        print(self.csv_sep)
        # self.csv_oct = './September.xlsx'
        self.raw_df = pd.read_excel(self.csv_sep, header=1, index_col=0)
        self.df = spa.adapt_column_names(self.raw_df)
        self.df = spa.check_SP_integrity(self.df)

    def test_adapt_column_names_check_for_blanks_in_col_names(self):
        df_with_renamed_columns = spa.adapt_column_names(self.raw_df)
        actual_col_names = df_with_renamed_columns.columns
        for name in actual_col_names:
            self.assertFalse(name[-1] == ' ', "the column name {0} contains a trailing blanks space".format(name))

    def test_adapt_column_names_check_values(self):
        df_with_renamed_columns = spa.adapt_column_names(self.raw_df)
        actual_col_names = df_with_renamed_columns.columns
        wanted_col_names = ["SERIAL_NUMBER", "HELP_DESK/_TSG", "COUNTRY", "ACCOUNT", "ACCOUNT_CLASS", "FIRST_NAME",
                            "LAST_NAME",
                            "CASE_PRODUCT", "LANGUAGE", "REGION", "FUNCTION", "CONTACT_CHANNEL", "TRANSFER/_DIRECT",
                            "CASE_NUMBER",
                            "DATE_OPENED", "DATE_CLOSED", "TIME_TO_RESOLVE_IN_HRS_(INC_OH)",
                            "TIME_TO_RESOLVE_IN_HRS_(EXC_OH)",
                            "RESOLVED_IN_30_MINUTES", "RESOLUTION_TIME_BUCKETS", "CASE_SUBJECT", "DESCRIPTION",
                            "CASE_SYMPTOM",
                            "DIAGNOSIS", "ISSUE_TYPE", "PRODUCT_VERSION", "SEVERITY", "RESOLUTION_COMMENT",
                            "CREATED_BY",
                            "CREATED_BY_GROUP", "CASE_OWNER", "CASE_OWNER_ROLE", "SERVICE_RESTORED_BY",
                            "SERVICE_RESTORED_BY_GROUP",
                            "HELP_DESK_SEGMENT", "TSG_SEGMENT", "RELATIONSHIP_MODEL", "BUSINESS_CHANNEL", "GGO_COUNTRY",
                            "GGO_REGION/_TSG", "NO_CLIENT_CONTACT_FLAG", "TEAM_TYPE", "FRONTLINE_TEAM_SUPPORT",
                            "CENTER/PRODUCT_FAMILY",
                            "CAUSE", "CLOSURE_CODE", "CASE_RECORD_TYPE", "VIP_CASES_INDICATOR", "PRODUCT_CAPABILITY",
                            "CASE_OWNER_EMPLOYEE_NUMBER", "CASE_ORIGIN", "TIME_TO_1ST_CALL_BACK",
                            "TIME_TO_CLOSE_IN_HRS_(INC_OH)",
                            "TIME_TO_CLOSE_IN_HRS_(EXC_OH)", "CLOSED_IN_30_MINUTES", "CLOSURE_TIME_BUCKETS",
                            "ACCOUNT_SITE", "CST_TOUCHED"
            , "TSG_TOUCHED", "VISIT_FLAG", "REMOTE_SUPPORT_FLAG", "SECTOR", "CASE_FLAG", "INBOUND/PROACTIVE",
                            "TARGET_MAPPING", "TSG/TECHNICAL", "TSG_SEGMENT", "CONTENT", "SPECIALISTS", "ASE",
                            "SERVICE_PULSE",
                            "CUSTOMER_COMMENTS", "Date_of_Interview", "Month", "Quarter"]

        diff = set(wanted_col_names).difference(set(actual_col_names))
        self.assertTrue(len(diff) == 0, "following column names differ: {0}".format(diff))

    def test_replace_column(self):
        self.assertTrue(True)

    #     def test_convert_column_to_integers(self):
    #         self.assertTrue(False)


    #     def test_filter_entitled(self):
    #         self.assertTrue(False)

    #
    #     def test_filter_winners(self):
    #         pass
    #



    def test_filter_team(self):
        df = spa.filter_team(self.df, ["HD_TECH_GER"])
        count = len(df.index)

        self.assertEqual(count, 12,
                         "The number of SP for HD_TECH_GER in September should be 12. It is {0} instead".format(count))

    def test_filter_agents(self):
        agent_list = ["Sabrina Klinner", "Anna Paszul"]
        df = spa.filter_agents(self.df, agent_list)
        count = len(df.index)
        self.assertEqual(count, 8,
                         "The number of SP for Anna P. and Sabrina K. in September should be 9. It is {0} instead".format(
                             count))

    #
    #     def test_prepare_raw_SP_report(self):
    #         pass
    #

    def test_calculate_avg_SPs(self):
        # calculate_avg_SP should return a
        # sp_averages = pyservicepulse.calculate_avg_SP(self.df)
        name = "Piotr Szymura"
        # avg_SP = sp_averages.ix[name].SP_average
        avgs = spa.calculate_avg_SPs(self.df)
        avg_SP_for_Piotr = avgs.ix[name]
        self.assertAlmostEqual(avg_SP_for_Piotr, 9.2, 4,
                               "The Service Pulse average for Piotr Sz. for the month September should be 9.2000. It is {0} instead".format(
                                   avg_SP_for_Piotr))
        name = "Sabrina Klinner"
        avg_SP_for_Sabrina = avgs.ix[name]
        self.assertAlmostEqual(avg_SP_for_Sabrina, 8.6667, 4,
                               "The Service Pulse average for Sabrina K. for the month September should be 8.666667. It is {0} instead".format(
                                   avg_SP_for_Sabrina))

    #     def test_merge_new_results(self):
    #         pass

    def test_filter_timespan(self):
        pass

    def test_import_new_data(self):
        pass
        #
        #     def test_update_raw_data(self):
        #         pass
        #
        #     def test_export_to_xls(self):
        #         pass
        #
        #     def test_send_email(self):
        #         pass
        #

