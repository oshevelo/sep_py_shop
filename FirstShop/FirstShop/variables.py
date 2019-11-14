class DeliveryStatus:
    WaitForSender = 1
    DeletedForm = 2
    NumberNotFound = 3
    DeliveryInOblast = 4
    DeliveryInLocal = 41
    DeliveryOnTheWay = 5
    DeliveryInTheCity = 6
    DeliveryOnTheBranch_1 = 7
    DeliveryOnTheBranch_2 = 8
    DeliveryReceived = 9
    DeliveryReceivedCashback = 10
    DeliveryReceivedCashbackGet = 11
    DeliveryReceivedCheck = 14
    OnTheWayToCustomer = 101
    RejectBySender_1 = 102
    RejectBySender_2 = 103
    RejectBySender_3 = 108
    DeliveryAddressChange = 104
    DeliveryHoldEnd = 105
    DeliveryBack = 106


class DeliveryProvider(object):
    novaposhta = 'Nova Poshta'
    justin = 'Justin'
    pickup = 'Pickup'


