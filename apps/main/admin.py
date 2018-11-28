import xadmin

# 全局配置
from xadmin import views

from apps.main.models import Navigation, Shop, User, Review, Banner, Category, Order, Property, PropertyValue, ShopCar, \
    Image, SubMenu, SubMenu2


class BaseStyleSettings:
    # 开启主题的修改
    enable_themes = True
    # 使用bootstrap的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSettings)


class GlobalSettings:
    # 修改标题
    site_title = '行云商城'
    # 修改底部显示
    site_footer = '行云科技有限责任公司'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class NavigationAdmin:
    # 默认情况下显示object对象
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationAdmin)


class ShopAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_id', 'name', 'sub_title', 'create_date']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['name', 'sub_title']


xadmin.site.register(Shop, ShopAdmin)


class ReviewAdmin:
    # 默认情况下显示object对象
    list_display = ['review_id', 'content', 'create_date', 'user']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['content', 'create_date']


xadmin.site.register(Review, ReviewAdmin)


class BannerAdmin:
    # 默认情况下显示object对象
    list_display = ['banner_id', 'title', 'image', 'detail_url', 'order', 'create_time']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['image', 'banner_id']


xadmin.site.register(Banner, BannerAdmin)


class CategoryAdmin:
    # 默认情况下显示object对象
    list_display = ['cate_id', 'name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['cate_id', 'name']


xadmin.site.register(Category, CategoryAdmin)


# class OrderAdmin:
#     # 默认情况下显示object对象
#     list_display = ['oid', 'order_code', 'address', 'post', 'receiver', 'mobile', 'user_message', 'create_date',
#                     'pay_date', 'delivery_date', 'confirm_date', 'status']
#     # 修改分页的默认的条数
#     list_per_page = 10
#     # 添加搜索字段
#     search_fields = ['order_code', 'oid', 'address', 'receiver', 'mobile']
#
#
# xadmin.site.register(Order, OrderAdmin)


class PropertyAdmin:
    # 默认情况下显示object对象
    list_display = ['property_id', 'name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['property_id', 'name']


xadmin.site.register(Property, PropertyAdmin)


class PropertyValueAdmin:
    # 默认情况下显示object对象
    list_display = ['pro_value_id', 'value']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['pro_value_id', 'value']


xadmin.site.register(PropertyValue, PropertyValueAdmin)


class ShopCarAdmin:
    # 默认情况下显示object对象
    list_display = ['car_id', 'number']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['car_id', 'number']


xadmin.site.register(ShopCar, ShopCarAdmin)


class ImageAdmin:
    # 默认情况下显示object对象
    list_display = ['shop_img_id', 'type']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['shop_img_id', 'type']


xadmin.site.register(Image, ImageAdmin)


class SubMenuAdmin:
    # 默认情况下显示object对象
    list_display = ['sub_menu_id', 'name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['sub_menu_id', 'name']


xadmin.site.register(SubMenu, SubMenuAdmin)


class SubMenu2Admin:
    # 默认情况下显示object对象
    list_display = ['sub_menu2_id', 'name']
    # 修改分页的默认的条数
    list_per_page = 10
    # 添加搜索字段
    search_fields = ['sub_menu2_id', 'name']


xadmin.site.register(SubMenu2, SubMenu2Admin)

# ==================自定义的admin========================================
# 自定义的admin
from xadmin.plugins import auth


# 显示自定义的方式
class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'email', 'img_show']


# 先注销
xadmin.site.unregister(User)
# 在注册
xadmin.site.register(User, UserAdmin)

# ==================END自定义的admin========================================
