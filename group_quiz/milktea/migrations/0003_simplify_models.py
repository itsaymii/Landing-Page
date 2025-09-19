# Generated migration to simplify models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milktea', '0002_category_ingredient_size_and_more'),
    ]

    operations = [
        # Remove unused models
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        
        # Remove unused fields from Product
        migrations.RemoveField(
            model_name='product',
            name='available_sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='product',
            name='preparation_time',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        
        # Rename base_price to price
        migrations.RenameField(
            model_name='product',
            old_name='base_price',
            new_name='price',
        ),
        
        # Update Review model
        migrations.RenameField(
            model_name='review',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='review',
            name='is_verified',
        ),
        
        # Update field types
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]