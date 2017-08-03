
import MySQLdb
import time
import multiprocessing.dummy

table_names = ['adjgiftreg_event', 'adjgiftreg_item', 'adjgiftreg_item_option', 'adjgiftreg_order', 'adjgiftreg_thank', 'adjgiftreg_type',
    'adjgiftreg_type_title','aitsys_news','aitsys_status','am_landing_page','am_landing_page_store','am_meta_config','am_shopby_filter',
    'am_shopby_page','am_shopby_range','am_shopby_value','amasty_amconf_attribute','amasty_amconf_product_attribute','aw_blog',
    'aw_blog_cat','aw_blog_cat_store','aw_blog_comment','aw_blog_post_cat','aw_blog_store','aw_blog_tags','bannerslider','ebizmarts_autoresponder_backtostock',
    'ebizmarts_autoresponder_backtostock_alert','ebizmarts_autoresponder_review','ebizmarts_autoresponder_unsubscribe','ebizmarts_autoresponder_visited',
    'ecomdev_urlrewrite_category_relation','ecomdev_urlrewrite_category_request_path','ecomdev_urlrewrite_category_url_key','ecomdev_urlrewrite_duplicate',
    'ecomdev_urlrewrite_duplicate_aggregate','ecomdev_urlrewrite_duplicate_increment','ecomdev_urlrewrite_duplicate_key','ecomdev_urlrewrite_duplicate_updated',
    'ecomdev_urlrewrite_product_relation','ecomdev_urlrewrite_product_request_path','ecomdev_urlrewrite_product_url_key','ecomdev_urlrewrite_rewrite',
    'ecomdev_urlrewrite_root_category','ecomdev_urlrewrite_transliterate','eltrino_region_entity','fowara_attribute_option_color','fowara_colorindex',
    'fowara_emailcollector_emails','giftwrap','giftwrap_giftcard','giftwrap_item','giftwrap_selection','gtspeed_image','gtspeed_stat','m_feedexport_custom_attribute',
    'm_feedexport_feed','m_feedexport_feed_history','m_feedexport_feed_product','m_feedexport_mapping_category','m_feedexport_performance_aggregated',
    'm_feedexport_performance_click','m_feedexport_performance_order','m_feedexport_rule','m_feedexport_rule_feed','m_feedexport_rule_product',
    'm_feedexport_template','magemonkey_api_debug','magemonkey_async_orders','magemonkey_async_subscribers','magemonkey_bulksync_export','magemonkey_bulksync_import',
    'magemonkey_ecommerce360','magemonkey_mails_sent','magenotification','magenotification_extension_feedback','magenotification_extension_feedbackmessage',
    'magenotification_license','magenotification_log','manufacturer','mdg_giftregistry_entity','mdg_giftregistry_item','mdg_giftregistry_type',
    'rewards_catalogrule_label','rewards_catalogrule_product','rewards_currency','rewards_customer','rewards_customer_index_points','rewards_importer',
    'rewards_milestone_rule','rewards_milestone_rule_log','rewards_special','rewards_store_currency','rewards_transfer','rewards_transfer_reference','rewardsref_referral',
    'rewardssocial_customer','rewardssocial_facebook_like','rewardssocial_facebook_share','rewardssocial_google_plusone','rewardssocial_pinterest_pin',
    'rewardssocial_purchase_share','rewardssocial_referral_share','rewardssocial_twitter_tweet','shift4_timeout_log','springbot_actions','springbot_cron_count',
    'springbot_cron_queue','springbot_redirect','springbot_redirect_order','springbot_trackable','store_locations','store_presss']

p = multiprocessing.dummy.Pool(4)

source_db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
    db = 'bdjeff_backup'
)

destination_db = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345',
    db = 'bdjeff_test'
)

source_cur = source_db.cursor()
destination_cur = destination_db.cursor()

def execute_thread(table):
    try:
        destination_cur.execute('create table bdjeff_test.{0} like bdjeff_backup.{1}' .format(table, table))
        destination_cur.execute('insert into bdjeff_test.{0} select * from bdjeff_backup.{1}' .format(table, table))
    except MySQLdb.OperationalError, e:
        print e


p.map(execute_thread, table_names)

# for table in table_names:
#     try:
#         t1 = threading.Thread(target=executes, args=(table))
#         t1.start()
#         t1.join()
#     except MySQLdb.OperationalError, e:
#         if e[1].startswith('Invalid'):
#             print table, '--->',  e[1].split()[-1].strip("''")
