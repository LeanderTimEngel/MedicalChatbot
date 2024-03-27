package org.example;
import org.jsoup.*;
import org.jsoup.nodes.*;
import org.jsoup.select.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import java.util.ArrayList;
import java.util.List;



public class Main {
    public static void main(String[] args) throws IOException {
        // initializing the HTML Document page variable

        Document pageDoc;
        Document loc;
        Document threaddoc;
        int skips = 0;
        int y;
        boolean diagTest;
        System.setProperty("sun.net.client.defaultConnectTimeout", "60000"); // 1min
        System.setProperty("sun.net.client.defaultReadTimeout", "60000"); // 1min

        StringBuilder builder = new StringBuilder();
        boolean start = true;
        ArrayList<report> reportList = new ArrayList<>();
        List<String> lines = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader("bereits geparste Diagnose .txt"));
        String line;
        while ((line = reader.readLine()) != null) {
            lines.add(line);
        }
        reader.close();
        CSVwriter csVwriter = new CSVwriter("csv zum schreiben der Daten");
        int i = 0;
        try {
            // fetching the target website
            pageDoc = Jsoup
                    .connect("URL zum scrapen")
                    .userAgent("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0")
                    .header("Accept-Language", "*")
                    .get();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Elements alphabetLinks = pageDoc.select("nav.az-list.u-mb a");

        for (Element alphabetLink : alphabetLinks) {
            if (!alphabetLink.hasClass("active") && !start) {
                String pageUrl = alphabetLink.attr("href");
                String forumUrl = "https://patient.info/" + pageUrl;
                pageDoc = Jsoup.connect(forumUrl).userAgent("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0").header("Accept-Language", "*").get();
            }
            start = false;
                // Scrape the content of the page here

        /*This Block gets the diagnosis and opens the threadlist for that type of diagnosis*/
            //Elements diagnosisRows = doc.select("tr.row-0");
            Elements diagnoses = pageDoc.select("table.table tr.row-0 td");
                for(Element diagnose : diagnoses){
                    diagTest = false ;
                    String Diagnosis = diagnose.select("a").text();
                    for(y=0; y<lines.size(); y++) {
                        if (Diagnosis.equals(lines.get(y))) {
                            diagTest = true;
                        }
                    }
                    if(diagTest){
                        continue;
                    }
                    String baseURL = "basis URL";
                    String extension = String.valueOf(diagnose.childNode(0).attributes());
                    String[] split = extension.split("\"");
                    extension = split[1];
                    String url = baseURL+extension;


                    try{
                        loc = Jsoup
                                .connect(url)
                                .userAgent("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0")
                                .header("Accept-Language", "*")
                                .get();
                    }catch (IOException e) {
                    throw new RuntimeException(e);

                    }
                    while(true) {
                        Elements threadlist = loc.select("li.disc-smr.cardb");
                        for (Element thread : threadlist) {
                            //sleep.sleeper();
                            extension = String.valueOf(thread.select("a[href]"));
                            split = extension.split("\"");
                            extension = split[1];
                            url = baseURL + extension;
                            try {
                                threaddoc = Jsoup
                                        .connect(url)
                                        .userAgent("Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0")
                                        .header("Accept-Language", "*")
                                        .get();
                            } catch (IOException e) {
                                sleep.sleeper(60000);
                                skips += 1;
                                System.out.println("times skipped: "+skips);
                                continue;
                            }
                            Element threadtext = threaddoc.selectFirst("div.post__content");
                            if (threadtext != null) {
                                Elements paragraphs = threadtext.select("p:not(.post__stats)");
                                for (Element paragraph : paragraphs) {
                                    String text = paragraph.text();
                                    builder.append(text);

                                }
                                String result = builder.toString();
                                report newReport = new report(i,Diagnosis,result);
                                reportList.add(newReport);
                                builder.setLength(0);
                                i++;

                            }

                        }
                        Element aElement = loc.select("a.reply__control.reply-ctrl-last.link").first();
                        if (aElement != null) {
                        String nextButton = aElement.attr("href");
                            // Get the URL of the next page

                            // Load the next page
                            loc = Jsoup.connect(nextButton).get();
                        }else{
                            break;
                        }
                    }
                    System.out.println(Diagnosis);
                    FileWriter writer = new FileWriter("bereits geparste Diagnosen .txt", true);
                    writer.write(Diagnosis+"\n");
                    writer.close();
                    for(report x : reportList){
                        csVwriter.writeRow(x.i , x.label, x.text);

                    }
                    reportList.clear();

                }
        }

        // initializing the list of Java object to store
// the scraped data
        List<patientReport> patientReportList = new ArrayList<>();

// retrieving the list of product HTML elements
        Elements patientReports = pageDoc.select("header.slat.articleHeader.articles-with-ads.u-mt.u-mb");

// iterating over the list of HTML products
        for (Element report : patientReports) {
            patientReport PatientReport = new patientReport();
            // extracting the data of interest from the report HTML element
            // and storing it in pokemonProduct
            //PatientReport.setText(report.selectFirst("p").text());
            PatientReport.setDiagnosis(report.selectFirst("span").text());

            // adding pokemonProduct to the list of the scraped products
            patientReportList.add(PatientReport);
        }
        System.out.println(patientReportList);
    }
    //Problem the crawler restarts once its done with alle the a-diseases
}

