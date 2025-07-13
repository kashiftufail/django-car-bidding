import rules

@rules.predicate
def is_seller(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.is_seller

@rules.predicate
def is_bidder(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.is_bidder

rules.add_perm('cars.add_car', is_seller)
rules.add_perm('cars.place_bid', is_bidder)