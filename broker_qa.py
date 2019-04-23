# coding=utf-8
from delivery_thrift.clients.broker import BrokerThriftClient
from ox_delivery_thrift_service_broker.ttypes import SelectionIdentifier, AdRequestContext
from ox_delivery_thrift_common.ttypes import RequestCommon, Trace, ExperimentTag, E_ExperimentType

selection_id = "1615070594"
trace_name = "anuraj"
trace_id = "cloudtest201"
request_con = {
"idx": "0",
"ox.viewability.score":"0.3"
}

experiment = ExperimentTag(E_ExperimentType.EXPERIMENT,group_name="bid_reuse_cache_key", label="bid_reuse_vis")
type = "AdUnit"
common = RequestCommon(trace=Trace(trace_name, trace_id), performance=None, svc_versions=[], context={}, experiment=experiment)
adreqcontext = AdRequestContext(request_common = common )
selection = SelectionIdentifier(type=type, id=selection_id, context=request_con)
selection_ids = list()
broker = BrokerThriftClient()
selection_ids.append(selection)
ctx = {
"ox.internal.click.prefix": "http://qa-v2-i35-presets.del-qa.openx.net/w/1.0/rc?ee=lart&ptr=3b4fbd5a-07e5-4f72-b6ea-898abea5c25c&",
"ox.techno.device.manufacturer": "desktop",
"ox.geo.latlongsrc": "derived",
"ox.http.proto": "http",
"ox.internal.host": "qa-v2-i35-presets.del-qa.openx.net",
"ox.user.accepts.cookies": "true",
"tp.test.1615070360": "cturl=openx.com&tts=10&bidder=8881&bids=1615070371-1615070383-1615070453:bid_price:240000",
"ox.regs.gdpr": "false",
"ox.http.language": "en-US,en;q=0.9",
"ox.user.mkt.cookie.age": "15397013",
"ox.user.new": "false",
"ox.user.storage.id": "0cce778a-faaa-0060-2e5b-39c9cb29546e",
"tp.test.1615070365": "cturl=openx.com&tts=10&multi=true&bidder=8887&bids=1615070373-1615070392-1615070499:bid_price:220000",
"ox.user.xdi.eligible": "false",
"ox.bidder.eligible": "false",
"ox.internal.svc_versions": "gateway/16.125.0",
"ox.internal.fn": "notify_loss,self_monetization,new_perm_app,limit_adresponse_time,api_hard_delete,dmp,tapad,selling_rules_ui,video_exchange,floorrule,passback_test,criteo,realtime_guaranteed,browser_id,mediamath,audittrail,resolicit2,ng_ad_quality,mstr_report,market,adserver,user_data,realvu,lineitem_recycle,viewability,speed,ad_engagement,pmp,multipub_ui_switch,demand_partner_creative_id,contentval,chain,aq_delivery,ad_category_filtering,dfp_bidder,aps",
"ox.internal.platform_id": "4c566c61-31ac-438d-bea8-f7cc314b1c11",
"queasy.trace.id": "3b4fbd5a-07e5-4f72-b6ea-898abea5c25c",
"mondemand.owner": trace_name,
"ox.user.id": "0cce778a-faaa-0060-2e5b-39c9cb29546e",
"ox.internal.store.user.data": "true",
"ox.user.mkt.id": "40981beb-cb06-43ed-90f3-ce05fa62487f",
"ox.techno.sw.name": "Chrome",
"ox.new_transaction_state": "1",
"ox.internal.rtb_partner": "true",
"ox.internal.debug": "true",
"ox.user.univ.id": "537072971|11694b56-0ef1-4f69-bb21-0cb5cc87059a|1552347311876091",
"ox.user.mkt.cookie.id": "40981beb-cb06-43ed-90f3-ce05fa62487f",
"tp.test.1615070364": "cturl=openx.com&tts=10&bidder=8885&bids=1615070376-1615070413-1615070523:bid_price:250000",
"mondemand.trace_id": trace_id,
"ox.user.storage.id.type": "m",
"ox.internal.medium": "web",
"ox.internal.tag_type": "iframe",
"ox.techno.os.version": "El Capitan",
"tp.test.1615070363": "cturl=openx.com&tts=10&bidder=8884&bids=1615070375-1615070404-1615089521:bid_price:260000",
"ox.techno.sw.version": "72",
"ox.regs.gdpr_source": "0",
"ox.user.mkt.new": "false",
"ox.user.mkt.accepts.cookies": "true",
"ox.http.user.agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
"ox.techno.os.type": "MacOSX",
"tp.test.1615070362": "cturl=openx.com&tts=10&bidder=8883&bids=1615070374-1615070400-1615070511:bid_price:190000",
"ox.user.dev.optout": "false",
"ox.internal.do.segmentation": "true",
"ox.techno.device.model": "browser",
"ox.techno.device.category": "desktop",
"ox.techno.device.type": "browser",
"ox.user.mkt.id.src": "cookie",
"tp.test.1615070361": "cturl=openx.com&tts=10&bidder=8882&bids=1615070370-1615070382-1615070450:bid_price:180000",
"ox.user.language": "en",
"ox.inventory.page_url": "http://openx.com",
"ox.user.ip": "10.1.253.2",
"ox.internal.perf.id": "3b4fbd5a-07e5-4f72-b6ea-898abea5c25c",
"tp.test.1615070366": "cturl=openx.com&tts=10&bidder=8886&bids=1615070372-1615070385-1615070486:bid_price:240000",
"ox.internal.perf.caller": "gateway",
"ox.viewability.score":"0.3"
}
broker.connect_to_service(host='qa-ox3-adserver-xv-04.xv.dc.openx.org', port=8082)

data = broker.client.requestAdChains(
            selection_ids=selection_ids,
            ad_request_context=adreqcontext,
            request_context=ctx
        )
print data
broker.disconnect_from_service()

# if str(data).find('buyer_8884') != -1:
#     print "buyer_8884 won the auction: Pass"
# else:
#     print "buyer_8884 not found in result: Fail"
