from __future__ import nested_scopes
from xml.dom import ValidationErr
from api.models import Singer, Song, Student
from rest_framework import serializers


#validator fxn
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should starts with R')
    return value
    

# class StudentSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100,validators=[starts_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
    
#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self,instance,validate_data): #instance refers to old data stored in db and validate_data is new data 
#         instance.id = validate_data.get('id',instance.id)
#         instance.name = validate_data.get('name',instance.name)
#         instance.roll = validate_data.get('roll',instance.roll)
#         instance.city = validate_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     #field level validator fxn
#     def validate_roll(self,value):
#         if value <= 100:
#             raise serializers.ValidationError('roll must be above 100')
#         return value

#     #obj level validator fxn
#     def validate(self,data):
#         name = data.get('name')
#         city = data.get('city')
#         print(data)
#         print(name, city)
#         if name.lower() == 'ram' and city.lower() != 'pokhara':
#             raise serializers.ValidationError('City must me pokhara')
#         return data
        
        
#ModelSerializer
class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True,validators = [starts_with_r])
    class  Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only':True}}
         
    #field level validator fxn
    def validate_roll(self,value):
        if value <= 100:
            raise serializers.ValidationError('roll must be above 100')
        return value

    #obj level validator fxn
    # def validate(self,data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == 'ram' and city.lower() != 'pokhara':
    #         raise serializers.ValidationError('City must me pokhara')
    #     return data


class SongSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField()
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']
        
# class SingerSerializer(serializers.ModelSerializer):
#     # songs = serializers.StringRelatedField(many=True,read_only=True)  #the attribute name is from related name attribute of foreign key in models
#     # songs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
#     # songs = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
#     songs = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='songs-detail')
#     class Meta:
#         model = Singer
#         fields = ['id','name','gender','songs']
        
# class SingerSerializer(serializers.HyperlinkedModelSerializer):
#     # songs = serializers.StringRelatedField(many=True,read_only=True)  #the attribute name is from related name attribute of foreign key in models
#     # songs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
#     # songs = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')
#     # songs = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='songs-detail')
#     songs = serializers.HyperlinkedIdentityField(many=True,view_name='song-detail')
#     class Meta:
#         model = Singer
#         fields = ['id','url','name','gender','songs']


#nested serializer
class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Singer
        fields = ['id','url','name','gender','songs']
    
    def create(self, validated_data):
        songs_data = validated_data.pop('songs')
        singer = Singer.objects.create(**validated_data)
        for song_data in songs_data:
            Song.objects.create(singer=singer, **song_data)
        return singer

    def update(self, instance, validated_data):
        songs_data = validated_data.pop('songs')
        songs = (instance.songs).all()
        print(songs)
        songs = list(songs)
        print(songs)
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        for song_data in songs_data:
            song = songs.pop(0)
            song.title = song_data.get('title', song.title)
            song.duration = song_data.get('duration', song.duration)
            song.save()
        instance.save()
        return instance
