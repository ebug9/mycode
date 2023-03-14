rooms = {

'Hall' : {
    'south' : 'Kitchen',
    'east'  : 'Dining Room',
    'item'  : 'key'
    },

'Kitchen' : {
    'north' : 'Hall',
    'item'  : 'monster'
    },

'Dining Room' : {
    'west'  : 'Hall',
    'south' : 'Garden',
    'east'  : 'Lounge',
    'item'  : 'potion'
    },

'Lounge' : {
    'west'  : 'Dining Room',
    'item'  : 'gemstone'
    },

'Garden' : {
    'north' : 'Dining Room'
    }

}
