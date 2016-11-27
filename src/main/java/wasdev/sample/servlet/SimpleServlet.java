package wasdev.sample.servlet;

import java.io.IOException;
import java.io.StringReader;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import weka.classifiers.Classifier;
import weka.classifiers.functions.MultilayerPerceptron;
import weka.core.Instances;
import weka.core.SerializationHelper;

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
        try {
            URL url = new URL("https://github.com/Catch2T8/uhac-1480208813071/raw/master/target/multilayerperceptron.model");
            MultilayerPerceptron model = (MultilayerPerceptron) SerializationHelper.read(url.openStream());
            String arff = "@RELATION credit\n\n"
                    + "   @ATTRIBUTE age  NUMERIC\n"
                    + "   @ATTRIBUTE sex  {male,female}\n"
                    + "   @ATTRIBUTE \"civil status\" {single,married}\n"
                    + "   @ATTRIBUTE children  NUMERIC\n"
                    + "   @ATTRIBUTE \"own car\" {yes,no}\n"
                    + "   @ATTRIBUTE house {rent,mortgage,parents,own}\n"
                    + "   @ATTRIBUTE subdivision {low class,mid class,first class}\n"
                    + "   @ATTRIBUTE employment {full,part}\n"
                    + "   @ATTRIBUTE \"net per annum\" NUMERIC\n"
                    + "   @ATTRIBUTE assets NUMERIC\n"
                    + "   @ATTRIBUTE liabilities NUMERIC\n"
                    + "   @ATTRIBUTE appraisal NUMERIC\n\n"
                    + "   @DATA\n"
                    + "22,male,single,0,no,parents,low class,full,185000,0,0";
            Instances instance = new Instances(new StringReader(arff));
            double result = model.classifyInstance(instance.instance(0));
            
        response.setContentType("text/html");
        response.getWriter().print(result);
        } catch (Exception ex) {
            response.setContentType("application/json");
            response.getWriter().print("{ \"message\" : \"Error :\"" + ex.getMessage() + "\" }");
        }
    }

}
