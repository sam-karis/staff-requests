from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from staffs.apps.staffs.models import RequestsCategory, StaffRequest
# local imports
from staffs.apps.staffs.serializers import (RequestsCategorySerializer,
                                            StaffRequestSerializer)
from staffs.helpers.email import send_email_notification
from staffs.helpers.permissions import IsAdminUserOrReadonly


class RequestCategoryAPIView(ListCreateAPIView):
    '''
    Handles get and add requests category
    '''
    permission_classes = (IsAdminUserOrReadonly, IsAuthenticated,)
    serializer_class = RequestsCategorySerializer
    queryset = RequestsCategory.objects.all()


class StaffRequestAPIView(APIView):
    '''
    Handles get all staff requests by admin
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = StaffRequestSerializer
    queryset = StaffRequest.objects.all()

    def post(self, request):
        request.data['employee'] = request.user.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'message': 'Expense request is successfully submitted.',
            'data': serializer.data
        }

        return Response(response, status=status.HTTP_200_OK)

    def get(self, request):
        user = request.user
        individual_requests = StaffRequest.objects.filter(employee=user)
        if individual_requests:
            serializer = StaffRequestSerializer(individual_requests, many=True)
            response = {
                'message': f'{request.user} expense requests submitted.',
                'data': serializer.data
            }
        else:
            response = {'message': 'You have no requests yet.'}

        return Response(response, status=status.HTTP_200_OK)


class GetStaffRequestAPIView(ListAPIView):
    '''
    Handles get all staff requests by admin
    '''
    permission_classes = (IsAdminUser, )
    serializer_class = StaffRequestSerializer
    queryset = StaffRequest.objects.all()


class ApproveRequestAPIView(APIView):
    '''
    Handles approving and disaproving staff requests by admin
    '''
    permission_classes = (IsAdminUser, )
    serializer_class = StaffRequestSerializer
    queryset = StaffRequest.objects.all()

    def get_request(self, id):
        try:
            return StaffRequest.objects.get(id=id)
        except StaffRequest.DoesNotExist:
            raise NotFound(f'No request id related to {id} id number.')

    def post(self, request, **kwargs):
        manager = request.user
        request_id = kwargs.get('request_id')
        staff_req = self.get_request(request_id)
        email = staff_req.employee.email
        request_status = request.data.get('status')
        if request_status not in ['approve', 'disapprove']:
            response = {
                'message': 'Must provided status field either approve or disapprove.'}  # noqa E501
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        context = {
            'username': staff_req.employee.username or email,
            'request_name': staff_req.request.name,
            'request_amount': staff_req.amount,
            'request_status': f'{request_status}d'
        }
        if staff_req.status in ['approve', 'disapprove']:
            message = "Staff request has already been approved or disapproved."
            return Response({'message': message})
        if manager.role.name in ['HR', 'People', 'Human Resource', 'Admin']:
            if staff_req.status == 'pending':
                message = "Line manager needs to approve the request first."
            elif staff_req.status == 'lm_stage':
                staff_req.status = request_status
                message = f"HR manager {request_status}d the request successfully."  # noqa E501
                send_email_notification([email], 'notification.html', context)
        elif staff_req.employee.line_manager == manager:
            if staff_req.status == 'pending':
                staff_req.status = 'lm_stage'
                message = f"Line manager {request_status}d the request successfully."  # noqa E501
            elif staff_req.status == 'lm_stage':
                message = "Line Manager has already approved or disapproved this request."  # noqa E501
            if request_status == 'disapprove':
                send_email_notification([email], 'notification.html', context)
        else:
            message = f"Only line manager can approve the request."
        staff_req.save()
        serializer = StaffRequestSerializer(staff_req)
        response = {'message': message, 'data': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
