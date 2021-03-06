from django.urls import path

from rms.views import views
from rms.views import warehouses as warehouses_views
from .api_views.inventory import *
from rmsv2.settings import COMPANY_SHORT

from rms.feeds import ReservationsFeed

urlpatterns = [
    path('', views.home_view, name='home'),

    path('search', views.search_view, name="search"),

    path('inventory/addDevice', views.add_device_view, name='add_device'),
    path('inventory/addInstance', views.create_instance_view, name='add_instance'),
    path('inventory/devices/<int:device_id>/delete', views.delete_device_view, name='delete_device'),
    path('inventory/devices/<int:device_id>/edit', views.edit_device_view, name='edit_device'),
    path('inventory/devices/<int:device_id>', views.device_view, name='device'),
    path('inventory/devices/<int:device_id>/instances/add', views.create_instance_view, name='create_instance'),
    path('inventory/devices/<int:device_id>/instances/<int:instance_id>',
         views.device_instance_view, name='device_instance'),
    path('inventory/devices/<int:device_id>/instances/<int:instance_id>/edit',
         views.edit_instance_view, name='edit_instance'),
    path('inventory/devices/<int:device_id>/instances/<int:instance_id>/delete',
         views.delete_instance_view, name='delete_instance'),
    path('inventory/devices/<int:device_id>/reservations', views.device_reservations_view, name='device_reservations'),

    path('inventory/categories/add', views.create_category_view, name='create_category'),
    path('inventory/categories/uncategorized', views.uncategorized_view, name='uncategorized'),
    path('inventory/categories/<int:category_id>', views.category_view, name='category'),
    path('inventory/categories/<int:category_id>/edit', views.edit_category_view, name='edit_category'),
    path('inventory/categories/<int:category_id>/delete', views.remove_category_view, name='delete_category'),

    path('settings/profile', views.profile_view, name='profile'),
    path('settings/profile/edit', views.edit_profile_view, name='edit_profile'),
    path('settings/profile/changePassword', views.change_password_view, name='change_password'),

    path('settings/users', views.users_list_view, name='users_list'),
    path('settings/users/add', views.create_user_view, name='create_user'),
    path('settings/users/<int:user_id>', views.user_view, name='user'),
    path('settings/users/<int:user_id>/edit', views.user_edit_view, name='edit_user'),
    path('settings/users/<int:user_id>/resetPassword', views.user_password_reset, name='user_password_reset'),
    path('settings/users/<int:user_id>/delete', views.delete_user_view, name='delete_user'),

    path('settings/groups', views.groups_list_view, name='groups_list'),
    path('settings/groups/add', views.add_group_view, name='add_group'),
    path('settings/groups/<int:group_id>', views.group_view, name='group'),
    path('settings/groups/<int:group_id>/edit', views.edit_group_view, name='edit_group'),
    path('settings/groups/<int:group_id>/delete', views.remove_group_view, name='remove_group'),
    path('settings/groups/<int:group_id>/modify', views.modify_group_view, name='modify_group'),

    path('reservations', views.reservations_view, name='reservations'),
    path('reservations/create', views.create_reservation_view, name='create_reservation'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>', views.reservation_view, name='reservation'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/edit',
         views.edit_reservation_view, name='edit_reservation'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/checkout',
         views.reservation_checkout_view, name='reservation_checkout'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/checkin',
         views.reservation_checkin_view, name='reservation_checkin'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/delete',
         views.remove_reservation_view, name='remove_reservation'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/devices/<int:device_id>/remove',
         views.remove_device_from_reservation, name="remove_device_from_reservation"),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/instances/<int:instance_id>/remove',
         views.remove_instance_from_reservation, name='remove_instance_from_reservation'),
    path('reservations/' + COMPANY_SHORT + '-<int:reservation_id>/export',
         views.reservation_pdf_generation, name='reservation_pdf'),

    path('customers', views.customers_view, name='customers'),
    path('customers/create', views.create_customer_view, name='create_customer'),
    path('customers/<int:customer_id>', views.customer_view, name="customer"),
    path('customers/<int:customer_id>/edit', views.edit_customer_view, name="edit_customer"),
    path('customers/<int:customer_id>/remove', views.remove_customer_view, name="remove_customer"),

    path('warehouses', warehouses_views.table_view, name='warehouses'),
    path('warehouses/add', warehouses_views.create_warehouse, name='add_warehouse'),
    path('warehouses/<int:warehouse_id>/edit', warehouses_views.edit_warehouse, name='edit_warehouse'),
    path('warehouses/<int:warehouse_id>/delete', warehouses_views.delete_warehouse, name='delete_warehouse'),

    path('api/inventory/tags/search', tag_search_view, name='api_tag_search'),
    path('api/inventory/tags/add', tag_add_view, name='api_tag_add'),
    path('api/inventory/devices/<int:device_id>/reservations/add',
         add_reservation_to_device, name="add_reservation_to_device"),
    path('api/inventory/devices/<int:device_id>/reservations',
         device_reservations_json, name="device_reservations_json"),
    path('api/inventory/instances/<int:instance_id>/reservations/add',
         add_instance_to_reservation, name="add_instance_to_reservation"),
    path('api/inventory/instances/<int:instance_id>/reservations',
         instance_reservations_json, name="instance_reservations_json"),

    path('api/reservations/'+COMPANY_SHORT+'-<int:reservation_id>/devices/<int:device_id>/changeAmount',
         edit_device_reservation, name="edit_device_reservation_amount"),
    path('api/reservations/'+COMPANY_SHORT+'-<int:reservation_id>/checkout',
         checkout_instance, name='api_reservation_checkout'),
    path('api/reservations/'+COMPANY_SHORT+'-<int:reservation_id>/checkin',
         checkin_instance, name='api_reservation_checkin'),
    path('api/reservations/'+COMPANY_SHORT+'-<int:reservation_id>/checkin_abstract',
         checkin_abstract_item, name="api_reservation_checkin_abstract"),

    path('feeds/ics/reservation.ics', ReservationsFeed(), name='reservations_feed'),
]
