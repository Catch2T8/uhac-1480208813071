package wasdev.sample.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class SimpleServlet
 */
@WebServlet("/SimpleServlet")
public class SimpleServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String age = request.getParameter("age");
        String sex = request.getParameter("sex");
        String civil = request.getParameter("civil");
        String children = request.getParameter("children");
        String car = request.getParameter("car");
        String house = request.getParameter("house");
        String subdivision = request.getParameter("subdivision");
        String employment = request.getParameter("employment");
        String annum = request.getParameter("annum");
        String assets = request.getParameter("assets");
        String liabilities = request.getParameter("liabilities");
        String appraisal = request.getParameter("appraisal");
        
        response.setContentType("text/html");
        response.getWriter().print("Hello World!");
        response.getWriter().print(age);
        response.getWriter().print(civil);
    }

}
