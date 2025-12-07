from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datasets.models import Dataset, Category
from django.utils import timezone


class Command(BaseCommand):
    help = 'Populate database with popular datasets'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('Populating Database with Popular Datasets'))
        self.stdout.write(self.style.SUCCESS('='*60 + '\n'))

        # Create categories
        self.stdout.write('Step 1: Creating categories...')
        categories = self.create_categories()
        self.stdout.write('')

        # Get or create user
        self.stdout.write('Step 2: Getting admin user...')
        user = self.get_admin_user()
        self.stdout.write('')

        # Add datasets
        self.stdout.write('Step 3: Adding popular datasets...')
        count = self.add_datasets(user, categories)
        self.stdout.write('')

        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(self.style.SUCCESS(f'✅ Successfully added {count} new datasets!'))
        self.stdout.write(self.style.SUCCESS('='*60 + '\n'))

    def create_categories(self):
        """Create common dataset categories"""
        categories_data = [
            {'name': 'Machine Learning', 'description': 'Datasets for machine learning and AI applications'},
            {'name': 'Computer Vision', 'description': 'Image and video datasets'},
            {'name': 'Natural Language Processing', 'description': 'Text and language datasets'},
            {'name': 'Business & Finance', 'description': 'Business, economics, and financial datasets'},
            {'name': 'Healthcare', 'description': 'Medical and healthcare datasets'},
            {'name': 'Social Sciences', 'description': 'Social science and demographic datasets'},
            {'name': 'Sports & Games', 'description': 'Sports statistics and game datasets'},
            {'name': 'Climate & Environment', 'description': 'Climate, weather, and environmental data'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created category: {cat_data["name"]}'))
            else:
                self.stdout.write(f'  - Category already exists: {cat_data["name"]}')

        return categories

    def get_admin_user(self):
        """Get or create admin user for datasets"""
        # Try to get existing superuser
        user = User.objects.filter(is_superuser=True).first()
        if user:
            self.stdout.write(f'  - Using existing superuser: {user.username}')
            return user

        # Create new admin user
        user = User.objects.create_user(
            username='dataideaorg',
            email='dataideaog@gmail.com',
            password='Chappie@256',
            first_name='DATA',
            last_name='IDEA',
        )
        user.is_staff = True
        user.is_superuser = True
        user.last_login = timezone.now()
        user.save()
        self.stdout.write(self.style.SUCCESS('  ✓ Created admin user'))
        return user

    def add_datasets(self, user, categories):
        """Add popular datasets"""
        datasets_data = [
            {
                'title': 'Iris Flower Dataset',
                'description': 'The classic Iris dataset contains measurements for 150 iris flowers from three different species. Perfect for learning classification algorithms and data visualization.',
                'file': 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                'file_size': 4,
                'file_type': 'CSV',
                'categories': ['Machine Learning'],
                'tags': 'classification, iris, flowers, beginner, UCI',
                'source_url': 'https://archive.ics.uci.edu/ml/datasets/iris',
                'license': 'CC0: Public Domain'
            },
            {
                'title': 'MNIST Handwritten Digits',
                'description': 'Database of 60,000 training images and 10,000 testing images of handwritten digits (0-9). A fundamental dataset for image classification and computer vision.',
                'file': 'http://yann.lecun.com/exdb/mnist/',
                'file_size': 11000,
                'file_type': 'Binary',
                'categories': ['Computer Vision', 'Machine Learning'],
                'tags': 'digits, handwriting, classification, deep learning, CNN',
                'source_url': 'http://yann.lecun.com/exdb/mnist/',
                'license': 'Creative Commons Attribution-Share Alike 3.0'
            },
            {
                'title': 'Titanic Dataset',
                'description': 'Passenger data from the Titanic including demographics and survival information. Perfect for binary classification and exploratory data analysis.',
                'file': 'https://www.kaggle.com/competitions/titanic/data',
                'file_size': 60,
                'file_type': 'CSV',
                'categories': ['Machine Learning', 'Social Sciences'],
                'tags': 'titanic, classification, kaggle, survival, beginner',
                'source_url': 'https://www.kaggle.com/competitions/titanic',
                'license': 'Database: Open Database, Contents: Database Contents'
            },
            {
                'title': 'COVID-19 Global Data',
                'description': 'Comprehensive COVID-19 pandemic data including cases, deaths, vaccinations, and testing statistics from countries worldwide. Updated regularly.',
                'file': 'https://github.com/owid/covid-19-data/tree/master/public/data',
                'file_size': 15000,
                'file_type': 'CSV',
                'categories': ['Healthcare', 'Social Sciences'],
                'tags': 'covid-19, pandemic, time series, health, global',
                'source_url': 'https://ourworldindata.org/coronavirus',
                'license': 'Creative Commons BY'
            },
            {
                'title': 'ImageNet',
                'description': 'Large-scale image dataset with over 14 million hand-annotated images belonging to 20,000+ categories. The gold standard for image classification.',
                'file': 'https://www.image-net.org/download.php',
                'file_size': 150000000,
                'file_type': 'Images',
                'categories': ['Computer Vision', 'Machine Learning'],
                'tags': 'images, classification, deep learning, benchmark, large-scale',
                'source_url': 'https://www.image-net.org/',
                'license': 'Custom - See website'
            },
            {
                'title': 'Movie Reviews Sentiment Analysis',
                'description': 'IMDB dataset of 50,000 movie reviews labeled for sentiment analysis. Balanced dataset with 25k positive and 25k negative reviews.',
                'file': 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
                'file_size': 84000,
                'file_type': 'Text/TAR',
                'categories': ['Natural Language Processing', 'Machine Learning'],
                'tags': 'sentiment analysis, NLP, text classification, movies, reviews',
                'source_url': 'https://ai.stanford.edu/~amaas/data/sentiment/',
                'license': 'Open Source'
            },
            {
                'title': 'Boston Housing Prices',
                'description': 'Housing data for 506 census tracts of Boston from the 1970 census. Contains 13 attributes used for predicting median home values.',
                'file': 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv',
                'file_size': 50,
                'file_type': 'CSV',
                'categories': ['Machine Learning', 'Business & Finance'],
                'tags': 'regression, housing, real estate, economics, Boston',
                'source_url': 'https://www.cs.toronto.edu/~delve/data/boston/bostonDetail.html',
                'license': 'Public Domain'
            },
            {
                'title': 'Wine Quality Dataset',
                'description': 'Physicochemical properties and quality ratings for red and white Portuguese "Vinho Verde" wines. Great for regression and classification tasks.',
                'file': 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/',
                'file_size': 340,
                'file_type': 'CSV',
                'categories': ['Machine Learning'],
                'tags': 'wine, quality, regression, classification, UCI',
                'source_url': 'https://archive.ics.uci.edu/ml/datasets/wine+quality',
                'license': 'CC BY 4.0'
            },
            {
                'title': 'Climate Change: Earth Surface Temperature',
                'description': 'Global land and ocean temperature data from 1750 to present. Includes temperature records from major cities worldwide.',
                'file': 'https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data',
                'file_size': 500000,
                'file_type': 'CSV',
                'categories': ['Climate & Environment'],
                'tags': 'climate change, temperature, time series, global warming, weather',
                'source_url': 'https://berkeleyearth.org/data/',
                'license': 'CC BY-NC-SA 4.0'
            },
            {
                'title': 'FIFA Players Dataset',
                'description': 'Comprehensive FIFA player statistics including ratings, positions, and attributes for thousands of professional soccer players.',
                'file': 'https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset',
                'file_size': 25000,
                'file_type': 'CSV',
                'categories': ['Sports & Games'],
                'tags': 'fifa, soccer, football, sports, players, statistics',
                'source_url': 'https://www.kaggle.com/stefanoleone992',
                'license': 'CC0: Public Domain'
            },
            {
                'title': 'New York City Taxi Trip Data',
                'description': 'Yellow and green taxi trip records including pickup/dropoff locations, times, fares, and passenger counts. Massive dataset for big data analysis.',
                'file': 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page',
                'file_size': 50000000,
                'file_type': 'CSV/Parquet',
                'categories': ['Business & Finance', 'Social Sciences'],
                'tags': 'transportation, NYC, taxi, big data, time series',
                'source_url': 'https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page',
                'license': 'Open Data'
            },
            {
                'title': 'Credit Card Fraud Detection',
                'description': 'Anonymized credit card transactions labeled as fraudulent or legitimate. Highly imbalanced dataset perfect for anomaly detection.',
                'file': 'https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud',
                'file_size': 150000,
                'file_type': 'CSV',
                'categories': ['Business & Finance', 'Machine Learning'],
                'tags': 'fraud detection, anomaly detection, finance, imbalanced, classification',
                'source_url': 'https://www.kaggle.com/mlg-ulb/creditcardfraud',
                'license': 'DbCL v1.0'
            },
            {
                'title': 'Human Activity Recognition (HAR)',
                'description': 'Smartphone sensor data from 30 volunteers performing six activities. Accelerometer and gyroscope readings for activity classification.',
                'file': 'https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones',
                'file_size': 25000,
                'file_type': 'Text',
                'categories': ['Machine Learning'],
                'tags': 'activity recognition, sensors, smartphones, time series, classification',
                'source_url': 'https://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones',
                'license': 'CC BY 4.0'
            },
            {
                'title': 'Amazon Product Reviews',
                'description': 'Large collection of Amazon product reviews including ratings, review text, and product metadata across multiple categories.',
                'file': 'https://nijianmo.github.io/amazon/index.html',
                'file_size': 50000000,
                'file_type': 'JSON',
                'categories': ['Natural Language Processing', 'Business & Finance'],
                'tags': 'reviews, sentiment, NLP, e-commerce, text mining',
                'source_url': 'https://nijianmo.github.io/amazon/index.html',
                'license': 'Research Use Only'
            },
            {
                'title': 'Breast Cancer Wisconsin',
                'description': 'Diagnostic breast cancer data with computed features from digitized images of fine needle aspirate. Binary classification task.',
                'file': 'https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)',
                'file_size': 125,
                'file_type': 'CSV',
                'categories': ['Healthcare', 'Machine Learning'],
                'tags': 'cancer, healthcare, diagnosis, classification, medical',
                'source_url': 'https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)',
                'license': 'CC BY 4.0'
            }
        ]

        created_count = 0
        for data in datasets_data:
            # Check if dataset already exists
            if Dataset.objects.filter(title=data['title']).exists():
                self.stdout.write(f'  - Dataset already exists: {data["title"]}')
                continue

            # Get categories
            dataset_categories = [categories[cat_name] for cat_name in data['categories']]

            # Create dataset
            dataset = Dataset.objects.create(
                title=data['title'],
                description=data['description'],
                file=data['file'],
                file_size=data.get('file_size'),
                file_type=data.get('file_type', 'Unknown'),
                tags=data['tags'],
                author=user,
                source_url=data.get('source_url', ''),
                license=data.get('license', '')
            )

            # Add categories
            dataset.categories.set(dataset_categories)
            dataset.save()

            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'  ✓ Added dataset: {data["title"]}'))

        return created_count