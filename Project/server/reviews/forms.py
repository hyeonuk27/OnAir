# from django import forms
# from django.forms import widgets
# from .models import Review, Comment


# class ReviewForm(forms.ModelForm):
#     title = forms.CharField(
#         label="Review Title",
#         label_suffix='',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '리뷰 제목을 작성해주세요',
#                 'maxlength': 50,
#                 'class': 'form-control',
#                 'style': 'margin: 0 auto;  width: 40%;',
#             }
#         )
#     )
    
#     content = forms.CharField(
#         label="Review Content",
#         label_suffix='',
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': '리뷰를 작성해주세요',
#                 'maxlength': 200,
#                 'class': 'form-control',
#                 'style': 'margin: 0 auto; width: 40%;',
#                 'size': 10,
#             }
#         )
#     )

#     rank = forms.IntegerField(
#         label="Rate",
#         label_suffix='',
#         widget=forms.NumberInput(
#             attrs={
#                 'placeholder': '1~10',
#                 'style': 'width: 8%; margin-left: 5px;',
#             }
#         )
#     )

#     class Meta:
#         model = Review
#         exclude = ('user', 'movie', 'like_users', 'movie_title',)


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(
#         label='',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '댓글을 작성해주세요.',
#                 'maxlength': 50,
#                 'style': 'width: 150%; margin-right: 10px;',
#             }
#         ),
#     )

#     class Meta:
#         model = Comment
#         exclude = ('review', 'user',)