# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Order.customer'
        db.delete_column(u'orders_order', 'customer_id')


    def backwards(self, orm):
        # Adding field 'Order.customer'
        db.add_column(u'orders_order', 'customer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['orders.Customer']),
                      keep_default=False)


    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 23, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'orders.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order'},
            'created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"})
        }
    }

    complete_apps = ['orders']