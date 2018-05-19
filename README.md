# yagna-assignment

Objective  Build an API-driven web-application for managing students enrolled in courses   
Technologies
  ● MySQL / PL-SQL
  ● Django
  ● HTML5, CSS3, JavaScript/Jqery   
Use Cases
    ● Students should be able to register using a username and password
    ● A student should be able to view the available courses
    ● A course can have a maximum of 5 enrolled students
    ● A student should be able to enroll or leave any number of courses
    ● A student should not be able to enroll into a completely booked course
    ● All users should be able to change their password 
    ● The admin user should be able to:
            • List all users
            • List all courses
            • List Students enrolled in a Course
            • Add/remove Students to Courses
            • Remove a Student
            • Add/remove a Course
 Specifications
      - Create RESTful endpoints for students and courses
      - The UI should make API requests to these endpoints and populate client-side templates
      - API tests for the following:
                - Course Listing
                - Course Enrolling
 my REST API has deploy in heroku web site
    
    this is REST API URL: https://lms-yagna.herokuapp.com
    
    End Points :
    
        https://lms-yagna.herokuapp.com/api/register/
                post format:{username:"","password":"","email":""}
        https://lms-yagna.herokuapp.com/api/accounts/login/
                login format: {"username":"", password:""}
        https://lms-yagna.herokuapp.com/api/accounts/logout/
        https://lms-yagna.herokuapp.com/api/accounts/change-password/
                change password formate : {"olPassword":"",newPassword:""}
        https://lms-yagna.herokuapp.com/api/admin/add-course/
                add course formate:: {"title":"","author":"","days":0,"courseDetails":""}
        https://lms-yagna.herokuapp.com/api/admin/remove-course/
                remove Course : {"courseId":0}
        https://lms-yagna.herokuapp.com/api/get-all/
        https://lms-yagna.herokuapp.com/api/student/enroll-course/
                enroll course : {"courseId":""} based on token
        https://lms-yagna.herokuapp.com/api/student/get-enroll-courses-by-student/
                get enrolled courses based on login user token
        https://lms-yagna.herokuapp.com/api/admin/remove-student-course/
                remove student {"studentId":0,"courseId":0}
        https://lms-yagna.herokuapp.com/api/admin/remove-student/
                removie student {"studentId":0}
        https://lms-yagna.herokuapp.com/api/admin/get-enrolled-students/
              
        https://lms-yagna.herokuapp.com/api/admin/get-students/
        https://lms-yagna.herokuapp.com/api/admin/add-to-course/
                 student add to course by admin {"studentId":0,"courseId":0}
                 
                 
        

